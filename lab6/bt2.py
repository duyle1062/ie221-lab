import requests
from bs4 import BeautifulSoup
import json
import csv
import time
from datetime import datetime

# Cấu hình
base_url = "https://vnexpress.net/thoi-su"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}

# Danh sách lưu trữ tất cả dữ liệu bài báo từ 5 trang
all_articles = []
page_statistics = []

print("=" * 60)
print("CRAWL DỮ LIỆU TỪ NHIỀU TRANG VNExpress")
print("=" * 60)

# Lặp qua 5 trang
for page_num in range(1, 6):
    try:
        # Xây dựng URL cho trang hiện tại
        if page_num == 1:
            url = base_url
        else:
            url = f"{base_url}-p{page_num}"

        print(f"\n[Trang {page_num}] Đang kết nối đến: {url}")

        # Gửi GET request
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()

        print(f"✓ Kết nối thành công! Status code: {response.status_code}")

        # Parse HTML
        soup = BeautifulSoup(response.content, "html.parser")

        # Tìm các phần tử chứa bài báo
        article_containers = soup.find_all("article") or soup.find_all(
            "div", class_="item-news"
        )

        # Nếu không tìm thấy, thử tìm các thẻ h3 với liên kết
        if len(article_containers) == 0:
            h3_elements = soup.find_all("h3")
            for h3 in h3_elements:
                link_tag = h3.find("a")
                if link_tag:
                    article_containers.append(h3)

        page_articles = 0

        # Trich xuất dữ liệu từ các bài báo
        for idx, container in enumerate(article_containers[:20]):
            try:
                # Tìm tiêu đề và liên kết
                title_tag = container.find("a") or container.find("h3", recursive=True)

                if title_tag:
                    title = title_tag.get_text(strip=True)

                    # Bỏ qua những bài báo không có tiêu đề
                    if not title:
                        continue

                    url_article = title_tag.get("href", "")

                    # Xử lý URL tương đối
                    if url_article and not url_article.startswith("http"):
                        url_article = "https://vnexpress.net" + url_article

                    # Tìm mô tả (thường trong thẻ <p> hoặc <span> hoặc <em>)
                    description = ""
                    desc_tag = (
                        container.find("p")
                        or container.find("span", class_="description")
                        or container.find("em")
                    )
                    if desc_tag:
                        description = desc_tag.get_text(strip=True)

                    # Thêm vào danh sách
                    article_info = {
                        "title": title,
                        "url": url_article,
                        "description": description,
                        "page": page_num,
                    }
                    all_articles.append(article_info)
                    page_articles += 1

                    # In ra thông tin bài báo
                    print(f"  {page_articles}. {title[:60]}")
                    if description:
                        print(f"     Mô tả: {description[:70]}...")

            except Exception as e:
                print(f"  ⚠ Lỗi xử lý bài báo: {e}")
                continue

        # Lưu thống kê trang
        page_statistics.append(
            {"page": page_num, "articles": page_articles, "url": url}
        )

        print(f"\n→ Trang {page_num}: {page_articles} bài báo")

        # Thêm độ trễ giữa các request (2 giây)
        if page_num < 5:
            print(f"⏳ Chờ 2 giây trước khi kết nối trang tiếp theo...")
            time.sleep(2)

    except requests.exceptions.RequestException as e:
        print(f"❌ Lỗi kết nối trang {page_num}: {e}")
    except Exception as e:
        print(f"❌ Lỗi không mong đợi (Trang {page_num}): {e}")

# Thống kê kết quả
print("\n" + "=" * 60)
print("THỐNG KÊ KẾT QUẢ")
print("=" * 60)

total_articles = len(all_articles)
total_pages = len(page_statistics)

if total_pages > 0:
    average_articles = total_articles / total_pages

    print(f"\n📊 TỔNG QUÁT:")
    print(f"  • Tổng số trang crawl: {total_pages}")
    print(f"  • Tổng số bài báo: {total_articles}")
    print(f"  • Số bài báo trung bình/trang: {average_articles:.1f}")

    print(f"\n📈 CHI TIẾT THEO TRANG:")
    for stat in page_statistics:
        print(f"  • Trang {stat['page']}: {stat['articles']} bài báo")

    # Tính toán thêm
    articles_with_desc = sum(1 for a in all_articles if a["description"])
    articles_without_desc = total_articles - articles_with_desc

    print(f"\n📝 THÔNG TIN MÔ TẢ:")
    print(f"  • Bài báo có mô tả: {articles_with_desc}")
    print(f"  • Bài báo không có mô tả: {articles_without_desc}")
    print(f"  • Tỷ lệ có mô tả: {(articles_with_desc/total_articles)*100:.1f}%")

    # Lưu dữ liệu vào file JSON
    json_filename = "vnexpress_multiple_pages.json"
    with open(json_filename, "w", encoding="utf-8") as json_file:
        json_data = {
            "crawl_time": datetime.now().isoformat(),
            "total_pages": total_pages,
            "total_articles": total_articles,
            "average_articles_per_page": average_articles,
            "articles": all_articles,
            "page_statistics": page_statistics,
        }
        json.dump(json_data, json_file, ensure_ascii=False, indent=2)

    print(f"\n✓ Đã lưu {total_articles} bài báo vào file {json_filename}")

    # Lưu dữ liệu vào file CSV
    csv_filename = "vnexpress_multiple_pages.csv"
    with open(csv_filename, "w", newline="", encoding="utf-8") as csv_file:
        writer = csv.DictWriter(
            csv_file, fieldnames=["page", "title", "url", "description"]
        )
        writer.writeheader()
        writer.writerows(all_articles)

    print(f"✓ Đã lưu {total_articles} bài báo vào file {csv_filename}")

    # Lưu thống kê trang vào file riêng
    stats_filename = "vnexpress_page_statistics.json"
    with open(stats_filename, "w", encoding="utf-8") as stats_file:
        json.dump(
            {
                "crawl_time": datetime.now().isoformat(),
                "page_statistics": page_statistics,
                "summary": {
                    "total_articles": total_articles,
                    "total_pages": total_pages,
                    "average_articles_per_page": average_articles,
                },
            },
            stats_file,
            ensure_ascii=False,
            indent=2,
        )

    print(f"✓ Đã lưu thống kê vào file {stats_filename}")

else:
    print("❌ Không có dữ liệu để xử lý!")

print("\n" + "=" * 60)
