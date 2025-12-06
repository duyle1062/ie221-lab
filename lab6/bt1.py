import requests
from bs4 import BeautifulSoup
import json
import csv
from datetime import datetime

# Cấu hình
url = "https://vnexpress.net/thoi-su"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}

try:
    # Gửi GET request
    print("Đang kết nối đến VNExpress...")
    response = requests.get(url, headers=headers, timeout=10)
    response.raise_for_status()  # Kiểm tra HTTP status code

    print(f"Kết nối thành công! Status code: {response.status_code}")

    # Parse HTML
    soup = BeautifulSoup(response.content, "html.parser")

    # Danh sách lưu trữ dữ liệu bài báo
    articles_data = []

    # Tìm các phần tử chứa bài báo
    # VNExpress sử dụng các cấu trúc khác nhau, ta sẽ thử nhiều cách
    article_containers = (
        soup.find_all("article")
        or soup.find_all("div", class_="item-news")
        or soup.find_all("div", class_="item-title")
    )

    print(f"Tìm thấy {len(article_containers)} bài báo")

    # Nếu không tìm thấy, thử tìm các thẻ h3 với liên kết
    if len(article_containers) == 0:
        h3_elements = soup.find_all("h3")
        for h3 in h3_elements[:20]:
            link_tag = h3.find("a")
            if link_tag:
                article_containers.append(h3)

    # Trich xuất dữ liệu từ các bài báo (tối đa 20)
    for idx, container in enumerate(article_containers[:20]):
        try:
            # Tìm tiêu đề và liên kết
            title_tag = container.find("a") or container.find("h3", recursive=True)

            if title_tag:
                title = title_tag.get_text(strip=True)
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
                }
                articles_data.append(article_info)

                # In ra console
                print(f"\n{idx + 1}. {title}")
                if description:
                    print(f"   Mô tả: {description[:100]}...")
                print(f"   URL: {url_article}")

        except Exception as e:
            print(f"Lỗi xử lý bài báo {idx + 1}: {e}")
            continue

    # Lưu vào file JSON
    if articles_data:
        json_filename = "vnexpress_articles.json"
        with open(json_filename, "w", encoding="utf-8") as json_file:
            json.dump(articles_data, json_file, ensure_ascii=False, indent=2)
        print(f"\n✓ Đã lưu {len(articles_data)} bài báo vào file {json_filename}")

    # Lưu vào file CSV
    if articles_data:
        csv_filename = "vnexpress_articles.csv"
        with open(csv_filename, "w", newline="", encoding="utf-8") as csv_file:
            writer = csv.DictWriter(
                csv_file, fieldnames=["title", "url", "description"]
            )
            writer.writeheader()
            writer.writerows(articles_data)
        print(f"✓ Đã lưu {len(articles_data)} bài báo vào file {csv_filename}")

    # In thống kê
    print(f"\n=== THỐNG KÊ ===")
    print(f"Tổng bài báo trich xuất: {len(articles_data)}")
    print(f"Bài báo có mô tả: {sum(1 for a in articles_data if a['description'])}")
    print(
        f"Bài báo không có mô tả: {sum(1 for a in articles_data if not a['description'])}"
    )

except requests.exceptions.RequestException as e:
    print(f"Lỗi kết nối: {e}")
except Exception as e:
    print(f"Lỗi không mong đợi: {e}")
