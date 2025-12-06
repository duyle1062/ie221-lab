import json
import string
import re
from collections import Counter
import matplotlib.pyplot as plt
from matplotlib import rcParams

# Set up Vietnamese font support
rcParams["font.sans-serif"] = ["Segoe UI", "Arial"]

# Load articles from Báo Thanh Niên
json_file = "thanhnien_articles.json"

try:
    with open(json_file, "r", encoding="utf-8") as f:
        data = json.load(f)

    print("=" * 70)
    print("PHÂN TÍCH TẦN SUẤT TỪ KHÓA TỪ TIÊU ĐỀ BÀI BÁO")
    print("=" * 70)
    print(f"\n📄 Đang tải dữ liệu từ: {json_file}")

    # Lấy tất cả tiêu đề từ các chuyên mục
    all_titles = []

    # Các chuyên mục trong file JSON
    categories = ["thoi_su", "kinh_te", "giao_duc", "cong_nghe", "the_thao"]

    for category in categories:
        if category in data and isinstance(data[category], list):
            for article in data[category]:
                if "title" in article and article["title"]:
                    all_titles.append(article["title"])

    print(f"✓ Tổng tiêu đề tải được: {len(all_titles)}")

    if len(all_titles) == 0:
        print("❌ Không tìm thấy tiêu đề nào!")
        exit(1)

    # 1. Xử lý văn bản
    print("\n" + "=" * 70)
    print("BƯỚC 1: XỬ LÝ VĂN BẢN")
    print("=" * 70)

    # Kết hợp tất cả tiêu đề
    combined_text = " ".join(all_titles)

    # Chuyển thành chữ thường
    combined_text = combined_text.lower()
    print("✓ Chuyển tất cả ký tự thành chữ thường")

    # Loại bỏ dấu câu
    # Giữ lại tiếng Việt và xóa dấu câu tiếng Anh
    combined_text = re.sub(
        r"[^\w\s\u00C0-\u017Fàáảãạăằắẳẵặâầấẩẫậèéẻẽẹêềếểễệìíỉĩịòóỏõọôồốổỗộơờớởỡợùúủũụưừứửữựỳýỷỵỹđ]",
        " ",
        combined_text,
    )
    print("✓ Loại bỏ dấu câu")

    # Tách từ dựa trên dấu cách
    words = combined_text.split()
    print(f"✓ Tách từ: {len(words)} từ được tách ra")

    # 2. Loại bỏ các từ không có ý nghĩa (stopwords)
    print("\n" + "=" * 70)
    print("BƯỚC 2: LỌC TỪ CÓ NGHĨA")
    print("=" * 70)

    # Danh sách stopwords tiếng Việt
    vietnamese_stopwords = {
        "và",
        "hay",
        "hoặc",
        "nhưng",
        "mà",
        "được",
        "là",
        "cái",
        "chiếc",
        "những",
        "nước",
        "người",
        "những",
        "có",
        "có",
        "từ",
        "đến",
        "về",
        "trên",
        "dưới",
        "của",
        "để",
        "theo",
        "như",
        "khi",
        "nếu",
        "thì",
        "vì",
        "mặc",
        "dù",
        "chứa",
        "hơn",
        "kém",
        "bằng",
        "chỉ",
        "mới",
        "vừa",
        "sẽ",
        "đã",
        "đang",
        "phải",
        "hay",
        "cùng",
        "lại",
        "hết",
        "cơn",
        "việc",
        "tại",
        "cả",
        "các",
        "a",
        "an",
        "and",
        "the",
        "is",
        "at",
        "on",
        "in",
        "or",
        "it",
        "be",
        "to",
        "as",
        "by",
        "for",
        "of",
        "with",
        "was",
        "were",
        "am",
        "are",
    }

    # Lọc từ: bỏ stopwords và từ ngắn (< 2 ký tự)
    filtered_words = [
        word
        for word in words
        if len(word) >= 2 and word not in vietnamese_stopwords and word.strip()
    ]

    print(f"✓ Số từ sau khi lọc: {len(filtered_words)}")
    print(f"✓ Bỏ đi {len(words) - len(filtered_words)} từ không có ý nghĩa/ngắn")

    # 3. Thống kê tần suất
    print("\n" + "=" * 70)
    print("BƯỚC 3: THỐNG KÊ TẦN SUẤT")
    print("=" * 70)

    # Đếm tần suất từ
    word_freq = Counter(filtered_words)

    # Lấy top 15 từ có tần suất cao nhất
    top_15_words = word_freq.most_common(15)

    print(f"\n🔝 TOP 15 TỪ KHÓA CÓ TẦN SUẤT CAO NHẤT:\n")
    print(f"{'STT':<4} {'Từ khóa':<30} {'Tần suất':<10} {'Biểu đồ'}")
    print("-" * 70)

    for i, (word, freq) in enumerate(top_15_words, 1):
        bar = "█" * freq
        print(f"{i:<4} {word:<30} {freq:<10} {bar}")

    # 4. Vẽ biểu đồ cột
    print("\n" + "=" * 70)
    print("BƯỚC 4: VẼ BIỂU ĐỒ")
    print("=" * 70)

    # Chuẩn bị dữ liệu cho biểu đồ
    words_list = [word for word, _ in top_15_words]
    frequencies = [freq for _, freq in top_15_words]

    # Tạo biểu đồ
    fig, ax = plt.subplots(figsize=(14, 8))

    # Vẽ các cột
    bars = ax.bar(
        range(len(words_list)),
        frequencies,
        color="steelblue",
        edgecolor="navy",
        linewidth=1.5,
    )

    # Tùy chỉnh trục x
    ax.set_xlabel("Từ khóa", fontsize=12, fontweight="bold")
    ax.set_ylabel("Tần suất xuất hiện", fontsize=12, fontweight="bold")
    ax.set_title(
        "TOP 15 TỪ KHÓA CÓ TẦN SUẤT CAO NHẤT TRONG TIÊU ĐỀ BÀI BÁO\n(Từ VNExpress và Báo Thanh Niên)",
        fontsize=14,
        fontweight="bold",
        pad=20,
    )

    # Đặt nhãn cho trục x
    ax.set_xticks(range(len(words_list)))
    ax.set_xticklabels(words_list, rotation=45, ha="right", fontsize=10)

    # Thêm giá trị tần suất trên mỗi cột
    for bar, freq in zip(bars, frequencies):
        height = bar.get_height()
        ax.text(
            bar.get_x() + bar.get_width() / 2.0,
            height,
            f"{int(freq)}",
            ha="center",
            va="bottom",
            fontsize=10,
            fontweight="bold",
        )

    # Tùy chỉnh lưới
    ax.grid(axis="y", alpha=0.3, linestyle="--")
    ax.set_axisbelow(True)

    # Điều chỉnh bố cục
    plt.tight_layout()

    # Lưu biểu đồ
    chart_file = "keyword_frequency_chart.png"
    plt.savefig(chart_file, dpi=300, bbox_inches="tight")
    print(f"\n✓ Biểu đồ đã được lưu: {chart_file}")

    # Hiển thị biểu đồ
    plt.show()

    # 5. Lưu kết quả vào file JSON
    print("\n" + "=" * 70)
    print("BƯỚC 5: LƯU KẾT QUẢ")
    print("=" * 70)

    analysis_result = {
        "total_articles": len(all_titles),
        "total_words": len(words),
        "total_filtered_words": len(filtered_words),
        "unique_words": len(word_freq),
        "top_15_keywords": [
            {"rank": i + 1, "keyword": word, "frequency": freq}
            for i, (word, freq) in enumerate(top_15_words)
        ],
        "all_keyword_frequencies": dict(word_freq.most_common(50)),
    }

    result_file = "keyword_analysis_result.json"
    with open(result_file, "w", encoding="utf-8") as f:
        json.dump(analysis_result, f, ensure_ascii=False, indent=2)

    print(f"✓ Kết quả phân tích lưu vào: {result_file}")

    # Thống kê cuối cùng
    print("\n" + "=" * 70)
    print("THỐNG KÊ CUỐI CÙNG")
    print("=" * 70)
    print(f"\n📊 Tổng số bài báo phân tích: {len(all_titles)}")
    print(f"📊 Tổng số từ trước lọc: {len(words)}")
    print(f"📊 Tổng số từ sau lọc: {len(filtered_words)}")
    print(f"📊 Số từ duy nhất: {len(word_freq)}")
    print(
        f"📊 Từ khóa xuất hiện nhiều nhất: '{top_15_words[0][0]}' ({top_15_words[0][1]} lần)"
    )

    # Thống kê thêm
    avg_word_length = (
        sum(len(word) for word in filtered_words) / len(filtered_words)
        if filtered_words
        else 0
    )
    print(f"📊 Độ dài từ trung bình: {avg_word_length:.2f} ký tự")

    # Tính phần trăm
    top_15_total = sum(freq for _, freq in top_15_words)
    total_filtered = len(filtered_words)
    percentage = (top_15_total / total_filtered * 100) if total_filtered > 0 else 0
    print(f"📊 Top 15 từ chiếm: {percentage:.1f}% tổng số từ đã lọc")

    print("\n" + "=" * 70)
    print("✓ HOÀN THÀNH PHÂN TÍCH")
    print("=" * 70 + "\n")

except FileNotFoundError:
    print(f"❌ Không tìm thấy file {json_file}")
    print("   Vui lòng chạy bt3.py trước để tạo dữ liệu!")
except Exception as e:
    print(f"❌ Lỗi: {e}")
    import traceback

    traceback.print_exc()
