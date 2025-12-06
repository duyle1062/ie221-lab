import requests
from bs4 import BeautifulSoup
import json
import time
from datetime import datetime
from urllib.parse import urljoin
import re

# Cấu hình
BASE_URL = "https://thanhnien.vn"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

# Các chuyên mục cần crawl
CATEGORIES = {
    "thoi_su": {
        "name": "Thời sự",
        "url": "https://thanhnien.vn/thoi-su.htm",
        "articles": [],
    },
    "kinh_te": {
        "name": "Kinh tế",
        "url": "https://thanhnien.vn/kinh-te.htm",
        "articles": [],
    },
    "giao_duc": {
        "name": "Giáo dục",
        "url": "https://thanhnien.vn/giao-duc.htm",
        "articles": [],
    },
    "cong_nghe": {
        "name": "Công nghệ",
        "url": "https://thanhnien.vn/cong-nghe.htm",
        "articles": [],
    },
    "the_thao": {
        "name": "Thể thao",
        "url": "https://thanhnien.vn/the-thao.htm",
        "articles": [],
    },
}


def extract_article_info(title_element, category_name):
    """Trích xuất thông tin bài báo từ h2/h3 element"""
    try:
        article_data = {
            "title": "",
            "url": "",
            "description": "",
            "author": "",
            "publish_date": "",
            "category": category_name,
            "thumbnail_url": "",
            "full_content": "",
            "views": "",
            "tags": [],
        }

        # Tìm tiêu đề và URL từ link
        title_link = title_element.find("a", class_="box-category-link-title")
        if title_link:
            article_data["title"] = title_link.get_text(strip=True)
            article_url = title_link.get("href", "")
            if article_url:
                article_data["url"] = urljoin(BASE_URL, article_url)

        # Tìm phần tử container (div cha của h2/h3)
        container = title_element.find_parent()

        # Tìm mô tả
        if container:
            desc_elem = container.find("p", class_="box-category-link-sapo")
            if desc_elem:
                article_data["description"] = desc_elem.get_text(strip=True)

            # Tìm hình ảnh
            img_elem = container.find("img")
            if img_elem:
                img_url = img_elem.get("src", "") or img_elem.get("data-src", "")
                if img_url and img_url.strip():
                    article_data["thumbnail_url"] = urljoin(BASE_URL, img_url)

            # Tìm tác giả
            author_elem = container.find("span", class_="box-category-link-author")
            if author_elem:
                article_data["author"] = author_elem.get_text(strip=True)

            # Tìm ngày xuất bản
            time_elem = container.find("span", class_="box-category-link-time")
            if time_elem:
                article_data["publish_date"] = time_elem.get_text(strip=True)

        return article_data

    except Exception as e:
        print(f"  ⚠ Lỗi trích xuất thông tin: {e}")
        return None


def get_article_details(article_url):
    """Truy cập trang chi tiết để lấy thêm thông tin"""
    try:
        response = requests.get(article_url, headers=headers, timeout=10)
        response.raise_for_status()

        soup = BeautifulSoup(response.content, "html.parser")

        detail_data = {"full_content": "", "views": "", "tags": []}

        # Tìm nội dung đầy đủ
        content_elem = soup.find("div", class_="detail-content-body")
        if not content_elem:
            content_elem = soup.find("div", class_="article-content")
        if not content_elem:
            content_elem = soup.find("div", id="article-content")

        if content_elem:
            paragraphs = content_elem.find_all("p")
            full_text = "\n".join(
                [p.get_text(strip=True) for p in paragraphs if p.get_text(strip=True)]
            )
            detail_data["full_content"] = full_text[:500] + (
                "..." if len(full_text) > 500 else ""
            )

        # Tìm số lượt xem
        views_elem = soup.find("span", class_="view-count")
        if views_elem:
            detail_data["views"] = views_elem.get_text(strip=True)

        # Tìm tags
        tag_elements = soup.find_all("a", class_="tag-link")
        if tag_elements:
            detail_data["tags"] = [tag.get_text(strip=True) for tag in tag_elements]

        return detail_data

    except requests.exceptions.Timeout:
        print(f"  ⚠ Timeout khi truy cập: {article_url}")
        return None
    except Exception as e:
        print(f"  ⚠ Lỗi khi truy cập chi tiết: {e}")
        return None


def crawl_category(category_key, category_info):
    """Crawl bài báo từ một chuyên mục"""
    print(f"\n{'='*70}")
    print(f"CRAWLING: {category_info['name']} ({category_key})")
    print(f"URL: {category_info['url']}")
    print(f"{'='*70}")

    try:
        # Gửi request đến trang chuyên mục
        response = requests.get(category_info["url"], headers=headers, timeout=10)
        response.raise_for_status()

        print(f"✓ Kết nối thành công (Status: {response.status_code})")

        # Parse HTML
        soup = BeautifulSoup(response.content, "html.parser")

        # Tìm các phần tử tiêu đề (h2 và h3 với class box-title-text)
        title_elements = soup.find_all(["h2", "h3"], class_="box-title-text")

        print(f"Tìm thấy {len(title_elements)} bài báo")

        articles_crawled = 0

        # Crawl tối đa 10 bài báo từ mỗi chuyên mục
        for idx, title_elem in enumerate(title_elements[:10]):
            try:
                # Trích xuất thông tin từ danh sách
                article_info = extract_article_info(title_elem, category_key)

                if not article_info or not article_info["url"]:
                    continue

                print(f"\n  {articles_crawled + 1}. {article_info['title'][:70]}")

                # Truy cập trang chi tiết
                detail_info = get_article_details(article_info["url"])

                if detail_info:
                    article_info.update(detail_info)

                if article_info["description"]:
                    print(f"     → Mô tả: {article_info['description'][:70]}")
                if article_info["author"]:
                    print(f"     → Tác giả: {article_info['author']}")
                if article_info["publish_date"]:
                    print(f"     → Ngày: {article_info['publish_date']}")

                category_info["articles"].append(article_info)
                articles_crawled += 1

                # Delay để tránh bị chặn
                time.sleep(1)

            except Exception as e:
                print(f"  ⚠ Lỗi xử lý bài báo {idx + 1}: {e}")
                continue

        print(f"\n→ Crawl xong {category_key}: {articles_crawled} bài báo")
        return articles_crawled

    except requests.exceptions.RequestException as e:
        print(f"❌ Lỗi kết nối: {e}")
        return 0
    except Exception as e:
        print(f"❌ Lỗi không mong đợi: {e}")
        return 0


def main():
    print("\n" + "=" * 70)
    print("CRAWL DỮ LIỆU TỪ BÁO THANH NIÊN - ĐA DẠNG CHỦ ĐỀ")
    print("=" * 70)
    print(f"Thời gian bắt đầu: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")

    # Crawl từng chuyên mục
    total_articles = 0
    category_stats = {}

    for category_key, category_info in CATEGORIES.items():
        articles_count = crawl_category(category_key, category_info)
        category_stats[category_key] = {
            "name": category_info["name"],
            "count": articles_count,
        }
        total_articles += articles_count

        # Delay giữa các chuyên mục
        if category_key != list(CATEGORIES.keys())[-1]:
            print(f"\n⏳ Chờ 2 giây trước khi crawl chuyên mục tiếp theo...")
            time.sleep(2)

    # Thống kê kết quả
    print("\n" + "=" * 70)
    print("THỐNG KÊ KẾT QUẢ")
    print("=" * 70)

    print(f"\n📊 TỔNG QUÁT:")
    print(f"  • Tổng số chuyên mục crawl: {len(CATEGORIES)}")
    print(f"  • Tổng số bài báo crawl được: {total_articles}")

    print(f"\n📈 CHI TIẾT THEO CHUYÊN MỤC:")
    for category_key, stats in category_stats.items():
        print(f"  • {stats['name']}: {stats['count']} bài báo")

    # Thống kê thêm
    articles_with_full_info = 0
    articles_missing_info = 0
    articles_with_author = 0
    articles_with_date = 0

    for category in CATEGORIES.values():
        for article in category["articles"]:
            if article["author"] and article["publish_date"]:
                articles_with_full_info += 1
            else:
                articles_missing_info += 1

            if article["author"]:
                articles_with_author += 1
            if article["publish_date"]:
                articles_with_date += 1

    print(f"\n📝 THÔNG TIN CHI TIẾT:")
    print(f"  • Bài báo có đầy đủ thông tin (author + date): {articles_with_full_info}")
    print(f"  • Bài báo có tác giả: {articles_with_author}")
    print(f"  • Bài báo có ngày xuất bản: {articles_with_date}")
    print(f"  • Bài báo thiếu thông tin: {articles_missing_info}")

    # Lưu dữ liệu vào JSON
    json_filename = "thanhnien_articles.json"
    json_data = {
        "crawl_time": datetime.now().isoformat(),
        "total_articles": total_articles,
        "categories_count": len(CATEGORIES),
        "category_statistics": category_stats,
    }

    # Thêm dữ liệu bài báo theo chuyên mục
    for category_key, category_info in CATEGORIES.items():
        json_data[category_key] = category_info["articles"]

    with open(json_filename, "w", encoding="utf-8") as f:
        json.dump(json_data, f, ensure_ascii=False, indent=2)

    print(f"\n✓ Đã lưu dữ liệu vào file {json_filename}")

    # Lưu thống kê chi tiết
    stats_filename = "thanhnien_statistics.json"
    stats_data = {
        "crawl_time": datetime.now().isoformat(),
        "summary": {
            "total_articles": total_articles,
            "total_categories": len(CATEGORIES),
            "articles_with_full_info": articles_with_full_info,
            "articles_with_author": articles_with_author,
            "articles_with_date": articles_with_date,
            "articles_missing_info": articles_missing_info,
        },
        "by_category": category_stats,
    }

    with open(stats_filename, "w", encoding="utf-8") as f:
        json.dump(stats_data, f, ensure_ascii=False, indent=2)

    print(f"✓ Đã lưu thống kê vào file {stats_filename}")

    print(f"\nThời gian kết thúc: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 70 + "\n")


if __name__ == "__main__":
    main()
