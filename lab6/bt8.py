import cv2
import numpy as np
import matplotlib.pyplot as plt
import os

print("=" * 80)
print("BÀI TẬP 8: CHUYỂN ĐỔI KHÔNG GIAN MÀU")
print("=" * 80)

# ============================================================================
# BƯỚC 1: TẢI ẢNH GỐC
# ============================================================================

print("\n" + "=" * 80)
print("BƯỚC 1: TẢI ẢNH GỐC (ẢNH MÀU BGR)")
print("=" * 80)

# Kiểm tra file photo.jpg
if not os.path.exists("photo.jpg"):
    print("\n❌ File photo.jpg không tìm thấy!")
    exit(1)

# Tải ảnh gốc (BGR format - mặc định của OpenCV)
image_bgr = cv2.imread("photo.jpg")

if image_bgr is None:
    print("❌ Lỗi: Không thể tải ảnh!")
    exit(1)

print("\n✓ Đã tải ảnh gốc: photo.jpg")
print(f"  - Kích thước: {image_bgr.shape[1]} × {image_bgr.shape[0]} pixel")
print(f"  - Shape: {image_bgr.shape}")
print(f"  - Không gian màu: BGR (mặc định của OpenCV)")
print(f"  - Data type: {image_bgr.dtype}")

# ============================================================================
# BƯỚC 2: CHUYỂN ĐỔI KHÔNG GIAN MÀU
# ============================================================================

print("\n" + "=" * 80)
print("BƯỚC 2: CHUYỂN ĐỔI KHÔNG GIAN MÀU")
print("=" * 80)

print("\n🎨 Chuyển đổi ảnh sang các không gian màu khác nhau:")
print("-" * 80)

# 1. Chuyển từ BGR sang RGB
print("\n1️⃣  BGR → RGB")
image_rgb = cv2.cvtColor(image_bgr, cv2.COLOR_BGR2RGB)
print(f"    ✓ Hoàn thành")
print(f"    ✓ Shape: {image_rgb.shape}")
print(f"    ✓ Mô tả: RGB (Red, Green, Blue) - định dạng tiêu chuẩn")

# 2. Chuyển sang Grayscale
print("\n2️⃣  BGR → Grayscale")
image_gray = cv2.cvtColor(image_bgr, cv2.COLOR_BGR2GRAY)
print(f"    ✓ Hoàn thành")
print(f"    ✓ Shape: {image_gray.shape}")
print(f"    ✓ Mô tả: Ảnh xám (1 kênh) - loại bỏ thông tin màu")

# 3. Chuyển sang HSV
print("\n3️⃣  BGR → HSV")
image_hsv = cv2.cvtColor(image_bgr, cv2.COLOR_BGR2HSV)
print(f"    ✓ Hoàn thành")
print(f"    ✓ Shape: {image_hsv.shape}")
print(f"    ✓ Mô tả: HSV (Hue, Saturation, Value)")
print(f"    ✓ Hue: 0-180 (trong OpenCV)")
print(f"    ✓ Saturation: 0-255")
print(f"    ✓ Value: 0-255")

# 4. Chuyển sang LAB
print("\n4️⃣  BGR → LAB")
image_lab = cv2.cvtColor(image_bgr, cv2.COLOR_BGR2LAB)
print(f"    ✓ Hoàn thành")
print(f"    ✓ Shape: {image_lab.shape}")
print(f"    ✓ Mô tả: LAB (L*, a*, b*) - không gian màu chuẩn hóa")
print(f"    ✓ L: 0-255 (độ sáng)")
print(f"    ✓ a: 0-255 (màu xanh-đỏ)")
print(f"    ✓ b: 0-255 (màu vàng-xanh)")

# 5. Chuyển sang YUV
print("\n5️⃣  BGR → YUV")
image_yuv = cv2.cvtColor(image_bgr, cv2.COLOR_BGR2YUV)
print(f"    ✓ Hoàn thành")
print(f"    ✓ Shape: {image_yuv.shape}")
print(f"    ✓ Mô tả: YUV (Luma, Chrominance)")
print(f"    ✓ Y: 0-255 (độ sáng)")
print(f"    ✓ U, V: 0-255 (thông tin màu)")

# ============================================================================
# BƯỚC 3: HIỂN THỊ ẢNH TRONG SUBPLOT
# ============================================================================

print("\n" + "=" * 80)
print("BƯỚC 3: HIỂN THỊ ẢNH TRONG SUBPLOT")
print("=" * 80)

print("\n📊 Tạo subplot với 6 ảnh:")
print("-" * 80)

# Tạo figure với 6 subplots (2 hàng, 3 cột)
fig, axes = plt.subplots(2, 3, figsize=(15, 10))
fig.suptitle(
    "Chuyển đổi Không Gian Màu (Color Space Conversion)", fontsize=16, fontweight="bold"
)

# Chuẩn bị dữ liệu hiển thị
# Các ảnh HSV, LAB, YUV cần chuyển đổi để hiển thị chính xác
image_hsv_display = cv2.cvtColor(image_hsv, cv2.COLOR_HSV2RGB)
image_lab_display = cv2.cvtColor(image_lab, cv2.COLOR_LAB2RGB)
image_yuv_display = cv2.cvtColor(image_yuv, cv2.COLOR_YUV2RGB)

# Danh sách ảnh và tiêu đề
images = [
    (image_rgb, "1. RGB", "Red, Green, Blue\nĐịnh dạng tiêu chuẩn"),
    (image_gray, "2. Grayscale", "Ảnh xám\n1 kênh"),
    (image_hsv_display, "3. HSV", "Hue, Saturation, Value\nBased on color perception"),
    (image_lab_display, "4. LAB", "L*, a*, b*\nNot gian màu chuẩn hóa"),
    (image_yuv_display, "5. YUV", "Luma, Chrominance\nSử dụng trong video"),
    (image_bgr[:, :, ::-1], "6. BGR (Gốc)", "Blue, Green, Red\nMặc định OpenCV"),
]

# Hiển thị các ảnh
for idx, (img, title, desc) in enumerate(images):
    row = idx // 3
    col = idx % 3
    ax = axes[row, col]

    if len(img.shape) == 2:  # Grayscale
        ax.imshow(img, cmap="gray")
    else:  # Color
        ax.imshow(img.astype(np.uint8))

    ax.set_title(title, fontsize=12, fontweight="bold")
    ax.set_xlabel(desc, fontsize=10)
    ax.axis("off")
    print(f"    ✓ {title}")

plt.tight_layout()

# Lưu subplot
subplot_file = "color_space_comparison.png"
plt.savefig(subplot_file, dpi=150, bbox_inches="tight")
print(f"\n✓ Lưu subplot: {subplot_file}")
print(f"  Size: {os.path.getsize(subplot_file) / 1024:.2f} KB")

# Hiển thị (nếu có GUI)
try:
    plt.show(block=False)
    plt.pause(2)
    plt.close()
    print("✓ Hiển thị subplot thành công")
except:
    print("⚠️  Lưu ý: Không thể hiển thị (GUI không khả dụng)")
    plt.close()

# ============================================================================
# BƯỚC 4: LƯU TẤT CẢ CÁC ẢNH ĐÃ CHUYỂN ĐỔI
# ============================================================================

print("\n" + "=" * 80)
print("BƯỚC 4: LƯU TẤT CẢ CÁC ẢNH ĐÃ CHUYỂN ĐỔI")
print("=" * 80)

print("\n💾 Lưu ảnh thành file riêng biệt:")
print("-" * 80)

# 1. Lưu ảnh RGB
rgb_file = "converted_rgb.jpg"
cv2.imwrite(rgb_file, cv2.cvtColor(image_rgb, cv2.COLOR_RGB2BGR))
print(f"\n1️⃣  RGB Image")
print(f"    ✓ File: {rgb_file}")
print(f"    ✓ Size: {os.path.getsize(rgb_file) / 1024:.2f} KB")
print(f"    ✓ Mô tả: Ảnh RGB - định dạng tiêu chuẩn")

# 2. Lưu ảnh Grayscale
gray_file = "converted_grayscale.jpg"
cv2.imwrite(gray_file, image_gray)
print(f"\n2️⃣  Grayscale Image")
print(f"    ✓ File: {gray_file}")
print(f"    ✓ Size: {os.path.getsize(gray_file) / 1024:.2f} KB")
print(f"    ✓ Mô tả: Ảnh xám - không có thông tin màu")

# 3. Lưu ảnh HSV (3 kênh riêng biệt)
hsv_file = "converted_hsv.jpg"
cv2.imwrite(hsv_file, image_hsv)
print(f"\n3️⃣  HSV Image")
print(f"    ✓ File: {hsv_file}")
print(f"    ✓ Size: {os.path.getsize(hsv_file) / 1024:.2f} KB")
print(f"    ✓ Mô tả: HSV - dựa trên cảm nhận màu sắc")
print(f"    ✓ Thường dùng cho: phát hiện màu, tách màu")

# 4. Lưu ảnh LAB
lab_file = "converted_lab.jpg"
cv2.imwrite(lab_file, image_lab)
print(f"\n4️⃣  LAB Image")
print(f"    ✓ File: {lab_file}")
print(f"    ✓ Size: {os.path.getsize(lab_file) / 1024:.2f} KB")
print(f"    ✓ Mô tả: LAB - không gian màu chuẩn hóa")
print(f"    ✓ Thường dùng cho: xử lý ảnh khoa học")

# 5. Lưu ảnh YUV
yuv_file = "converted_yuv.jpg"
cv2.imwrite(yuv_file, image_yuv)
print(f"\n5️⃣  YUV Image")
print(f"    ✓ File: {yuv_file}")
print(f"    ✓ Size: {os.path.getsize(yuv_file) / 1024:.2f} KB")
print(f"    ✓ Mô tả: YUV - sử dụng trong video/TV")
print(f"    ✓ Thường dùng cho: nén video")

# ============================================================================
# BƯỚC 5: TẠO ĐỒ THỊ SO SÁNH CÁC KÊNH
# ============================================================================

print("\n" + "=" * 80)
print("BƯỚC 5: TẠO ĐỒ THỊ SO SÁNH CÁC KÊNH MÀU")
print("=" * 80)

print("\n📈 Tạo histogram cho từng không gian màu:")
print("-" * 80)

# Tạo figure cho histogram
fig, axes = plt.subplots(3, 2, figsize=(14, 12))
fig.suptitle("Histogram So Sánh Không Gian Màu", fontsize=16, fontweight="bold")

# RGB Histogram
colors_rgb = ("r", "g", "b")
for i, color in enumerate(colors_rgb):
    hist = cv2.calcHist([image_rgb], [i], None, [256], [0, 256])
    axes[0, 0].plot(hist, color=color, label=f"{color.upper()} channel")
axes[0, 0].set_title("RGB - Histogram", fontweight="bold")
axes[0, 0].legend()
axes[0, 0].set_xlim([0, 256])

# Grayscale Histogram
hist_gray = cv2.calcHist([image_gray], [0], None, [256], [0, 256])
axes[0, 1].plot(hist_gray, color="gray")
axes[0, 1].set_title("Grayscale - Histogram", fontweight="bold")
axes[0, 1].set_xlim([0, 256])

# HSV Histogram
colors_hsv = ("h", "s", "v")
for i, color in enumerate(colors_hsv):
    hist = cv2.calcHist([image_hsv], [i], None, [256], [0, 256])
    axes[1, 0].plot(hist, label=f"{color.upper()} channel")
axes[1, 0].set_title("HSV - Histogram", fontweight="bold")
axes[1, 0].legend()
axes[1, 0].set_xlim([0, 256])

# LAB Histogram
colors_lab = ("L", "a", "b")
for i, color in enumerate(colors_lab):
    hist = cv2.calcHist([image_lab], [i], None, [256], [0, 256])
    axes[1, 1].plot(hist, label=f"{color} channel")
axes[1, 1].set_title("LAB - Histogram", fontweight="bold")
axes[1, 1].legend()
axes[1, 1].set_xlim([0, 256])

# YUV Histogram
colors_yuv = ("Y", "U", "V")
for i, color in enumerate(colors_yuv):
    hist = cv2.calcHist([image_yuv], [i], None, [256], [0, 256])
    axes[2, 0].plot(hist, label=f"{color} channel")
axes[2, 0].set_title("YUV - Histogram", fontweight="bold")
axes[2, 0].legend()
axes[2, 0].set_xlim([0, 256])

# BGR Histogram
colors_bgr = ("b", "g", "r")
for i, color in enumerate(colors_bgr):
    hist = cv2.calcHist([image_bgr], [i], None, [256], [0, 256])
    axes[2, 1].plot(hist, color=color, label=f"{color.upper()} channel")
axes[2, 1].set_title("BGR (Gốc) - Histogram", fontweight="bold")
axes[2, 1].legend()
axes[2, 1].set_xlim([0, 256])

plt.tight_layout()

# Lưu histogram
histogram_file = "color_space_histogram.png"
plt.savefig(histogram_file, dpi=150, bbox_inches="tight")
print(f"\n✓ Lưu histogram: {histogram_file}")
print(f"  Size: {os.path.getsize(histogram_file) / 1024:.2f} KB")

try:
    plt.show(block=False)
    plt.pause(2)
    plt.close()
    print("✓ Hiển thị histogram thành công")
except:
    print("⚠️  Lưu ý: Không thể hiển thị histogram (GUI không khả dụng)")
    plt.close()

# ============================================================================
# BƯỚC 6: THỐNG KÊ THÔNG TIN CHI TIẾT
# ============================================================================

print("\n" + "=" * 80)
print("BƯỚC 6: THỐNG KÊ THÔNG TIN CHI TIẾT")
print("=" * 80)

print("\n📊 BẢNG SO SÁNH CÁC KHÔNG GIAN MÀU:")
print("-" * 80)

color_spaces_info = [
    ("BGR (Gốc)", image_bgr, "Mặc định OpenCV - Blue, Green, Red"),
    ("RGB", image_rgb, "Tiêu chuẩn - Red, Green, Blue"),
    ("Grayscale", image_gray, "Ảnh xám - 1 kênh"),
    ("HSV", image_hsv, "Hue, Saturation, Value - cảm nhận màu"),
    ("LAB", image_lab, "L*, a*, b* - chuẩn hóa"),
    ("YUV", image_yuv, "Luma, Chrominance - video"),
]

print(f"\n{'Không gian màu':<15} {'Shape':<20} {'Channels':<12} {'Mô tả'}")
print("-" * 80)
for name, img, desc in color_spaces_info:
    if len(img.shape) == 2:
        shape_str = f"{img.shape}"
        channels = 1
    else:
        shape_str = f"{img.shape}"
        channels = img.shape[2]
    print(f"{name:<15} {shape_str:<20} {channels:<12} {desc}")

# ============================================================================
# BƯỚC 7: THÔNG TIN CHI TIẾT VỀ TỪNG KHÔNG GIAN MÀU
# ============================================================================

print("\n" + "=" * 80)
print("BƯỚC 7: THÔNG TIN CHI TIẾT VỀ TỪNG KHÔNG GIAN MÀU")
print("=" * 80)

details = {
    "RGB": """
    • Định dạng: 3 kênh (R, G, B)
    • Giá trị: 0-255 cho mỗi kênh
    • Ưu điểm: Tiêu chuẩn quốc tế, dễ hiển thị
    • Nhược điểm: Không tự nhiên với cảm nhận con người
    • Ứng dụng: Hiển thị, lưu trữ ảnh trên web
    """,
    "Grayscale": """
    • Định dạng: 1 kênh (độ sáng)
    • Giá trị: 0-255
    • Ưu điểm: Tiết kiệm bộ nhớ, xử lý nhanh
    • Nhược điểm: Mất thông tin màu
    • Ứng dụng: Xử lý ảnh cơ bản, phát hiện cạnh, nhận dạng
    """,
    "HSV": """
    • Định dạng: 3 kênh (H, S, V)
    • Giá trị: H(0-180), S(0-255), V(0-255) trong OpenCV
    • Ưu điểm: Tự nhiên với cảm nhận con người
    • Nhược điểm: Tính toán phức tạp hơn
    • Ứng dụng: Phát hiện màu, tách nền, xử lý màu
    """,
    "LAB": """
    • Định dạng: 3 kênh (L*, a*, b*)
    • Giá trị: L(0-255), a(0-255), b(0-255)
    • Ưu điểm: Chuẩn hóa, khoảng cách màu đúng
    • Nhược điểm: Tính toán phức tạp
    • Ứng dụng: Xử lý ảnh khoa học, quản lý màu
    """,
    "YUV": """
    • Định dạng: 3 kênh (Y, U, V)
    • Giá trị: Y(0-255), U(0-255), V(0-255)
    • Ưu điểm: Tách độ sáng và màu
    • Nhược điểm: Ít sử dụng trong ứng dụng hiện đại
    • Ứng dụng: Nén video, truyền hình
    """,
}

for color_space, detail in details.items():
    print(f"\n{color_space}:")
    print(detail)

# ============================================================================
# BƯỚC 8: TÓM LƯỢC
# ============================================================================

print("\n" + "=" * 80)
print("BƯỚC 8: TÓM LƯỢC KẾT QUẢ")
print("=" * 80)

output_files = [
    subplot_file,
    histogram_file,
    rgb_file,
    gray_file,
    hsv_file,
    lab_file,
    yuv_file,
]

print("\n📁 CÁC FILE ĐÃ TẠO:")
print("-" * 80)

total_size = 0
for fname in output_files:
    if os.path.exists(fname):
        size_kb = os.path.getsize(fname) / 1024
        total_size += size_kb
        print(f"  ✓ {fname:<30} {size_kb:>8.2f} KB")

print("-" * 80)
print(f"  📊 Tổng: {len(output_files)} file | Dung lượng: {total_size:.2f} KB")

print("\n📝 TÓMLƯỢC:")
print("-" * 80)
print(f"  • Ảnh gốc: photo.jpg ({image_bgr.shape[1]} × {image_bgr.shape[0]})")
print(f"  • Không gian màu: BGR → RGB, Grayscale, HSV, LAB, YUV")
print(f"  • Hiển thị: Subplot (6 ảnh) + Histogram")
print(f"  • Lưu file: 5 ảnh màu + 2 biểu đồ")

print("\n" + "=" * 80)
print("✅ BÀI TẬP 8 HOÀN THÀNH")
print("=" * 80)
print(f"\nSo sánh không gian màu đã được lưu vào:")
print(f"  • {subplot_file} (Subplot)")
print(f"  • {histogram_file} (Histogram)")
