import cv2
import numpy as np
import os

print("=" * 80)
print("BÀI TẬP 7: TẢI, ĐỌC VÀ HIỂN THỊ HÌNH ẢNH")
print("=" * 80)

# ============================================================================
# BƯỚC 1: CHUẨN BỊ FILE ẢNH
# ============================================================================

print("\n" + "=" * 80)
print("BƯỚC 1: CHUẨN BỊ FILE ẢNH")
print("=" * 80)

# Kiểm tra file photo.jpg
if not os.path.exists("photo.jpg"):
    print("\n❌ File photo.jpg không tìm thấy!")
    print("   Tạo ảnh test tự động...")

    # Tạo ảnh test
    width, height = 800, 600
    image = np.zeros((height, width, 3), dtype=np.uint8)

    # Nền gradient
    for y in range(height):
        for x in range(width):
            image[y, x] = [int(255 * y / height), 100, int(255 * x / width)]

    # Vẽ các hình dạng
    cv2.rectangle(image, (50, 50), (250, 200), (255, 255, 0), 3)
    cv2.circle(image, (400, 150), 80, (0, 255, 255), 3)
    pts = np.array([[600, 50], [700, 200], [500, 200]], np.int32)
    cv2.polylines(image, [pts], True, (0, 255, 0), 3)
    cv2.putText(
        image,
        "Test Image",
        (250, 400),
        cv2.FONT_HERSHEY_SIMPLEX,
        1.5,
        (255, 255, 255),
        2,
    )
    cv2.putText(
        image, "800x600", (300, 450), cv2.FONT_HERSHEY_SIMPLEX, 1, (200, 200, 200), 1
    )

    cv2.imwrite("photo.jpg", image)
    print("✓ Tạo file test image: photo.jpg")
else:
    print("✓ File photo.jpg đã tồn tại")

print(f"  File size: {os.path.getsize('photo.jpg') / 1024:.2f} KB")

# ============================================================================
# BƯỚC 2: TẢI ẢNH (Tải ảnh màu và xám)
# ============================================================================

print("\n" + "=" * 80)
print("BƯỚC 2: TẢI ẢNH (Ảnh màu và Ảnh xám)")
print("=" * 80)

# Tải ảnh màu (BGR format trong OpenCV)
image_color = cv2.imread("photo.jpg")
if image_color is None:
    print("❌ Lỗi: Không thể tải ảnh màu!")
    exit(1)

# Tải ảnh xám (grayscale)
image_gray = cv2.imread("photo.jpg", cv2.IMREAD_GRAYSCALE)
if image_gray is None:
    print("❌ Lỗi: Không thể tải ảnh xám!")
    exit(1)

print("\n✓ Đã tải ảnh màu và ảnh xám thành công")

# ============================================================================
# BƯỚC 3: LẤY THÔNG TIN ẢNH
# ============================================================================

print("\n" + "=" * 80)
print("BƯỚC 3: LẤY THÔNG TIN ẢNH")
print("=" * 80)

# Thông tin ảnh màu
print("\n📊 THÔNG TIN ẢNH MÀU:")
print("-" * 80)
color_shape = image_color.shape
color_height, color_width, color_channels = color_shape
print(f"1. Kích thước ảnh (width × height): {color_width} × {color_height}")
print(f"2. Shape (numpy array): {color_shape}")
print(f"   - Height (chiều cao): {color_height}")
print(f"   - Width (chiều rộng): {color_width}")
print(f"   - Channels (số kênh): {color_channels}")
print(f"3. Số chiều của numpy array: {image_color.ndim}")
print(f"4. Số kênh màu: {color_channels} (RGB: 3 kênh)")
print(f"5. Data type: {image_color.dtype}")
print(f"6. Tổng số pixel: {color_height * color_width}")
print(f"7. Dung lượng: {image_color.nbytes / 1024:.2f} KB")

# Thông tin ảnh xám
print("\n📊 THÔNG TIN ẢNH XÁM (GRAYSCALE):")
print("-" * 80)
gray_shape = image_gray.shape
gray_height, gray_width = gray_shape
print(f"1. Kích thước ảnh (width × height): {gray_width} × {gray_height}")
print(f"2. Shape (numpy array): {gray_shape}")
print(f"   - Height (chiều cao): {gray_height}")
print(f"   - Width (chiều rộng): {gray_width}")
print(f"3. Số chiều của numpy array: {image_gray.ndim}")
print(f"4. Số kênh màu: 1 (Grayscale: 1 kênh)")
print(f"5. Data type: {image_gray.dtype}")
print(f"6. Tổng số pixel: {gray_height * gray_width}")
print(f"7. Dung lượng: {image_gray.nbytes / 1024:.2f} KB")

# ============================================================================
# BƯỚC 4: HIỂN THỊ ẢNH
# ============================================================================

print("\n" + "=" * 80)
print("BƯỚC 4: HIỂN THỊ ẢNH (Các cửa sổ riêng biệt)")
print("=" * 80)

print("\n🖼️  Hiển thị ảnh:")
print("   1. Nhấn bất kỳ phím nào để đóng cửa sổ ảnh màu")
print("   2. Nhấn bất kỳ phím nào để đóng cửa sổ ảnh xám")
print("   (Nếu chạy trên server/CLI, bỏ qua hiển thị)")

try:
    # Hiển thị ảnh màu
    cv2.imshow("Color Image (Ảnh Màu)", image_color)
    print("✓ Hiển thị ảnh màu")
    cv2.waitKey(2000)  # Hiển thị 2 giây
    cv2.destroyWindow("Color Image (Ảnh Màu)")

    # Hiển thị ảnh xám
    cv2.imshow("Grayscale Image (Ảnh Xám)", image_gray)
    print("✓ Hiển thị ảnh xám")
    cv2.waitKey(2000)  # Hiển thị 2 giây
    cv2.destroyWindow("Grayscale Image (Ảnh Xám)")

    cv2.destroyAllWindows()
    print("✓ Đóng tất cả cửa sổ")
except Exception as e:
    print(f"⚠️  Lưu ý: Không thể hiển thị ảnh (GUI không khả dụng)")
    print(f"   Chi tiết: {str(e)}")

# ============================================================================
# BƯỚC 5: THAY ĐỔI KÍCH THƯỚC (RESIZE)
# ============================================================================

print("\n" + "=" * 80)
print("BƯỚC 5: THAY ĐỔI KÍCH THƯỚC (RESIZE)")
print("=" * 80)

print("\n📐 Resize ảnh thành các kích thước khác nhau:")
print("-" * 80)

# Resize thành 300x400
resized_300x400 = cv2.resize(image_color, (300, 400))
output_file_1 = "resized_300x400.jpg"
cv2.imwrite(output_file_1, resized_300x400)
print(f"\n1️⃣  Resize 300×400:")
print(f"    ✓ File: {output_file_1}")
print(f"    ✓ Shape: {resized_300x400.shape}")
print(f"    ✓ Size: {os.path.getsize(output_file_1) / 1024:.2f} KB")
print(f"    ✓ Kích thước: 300 × 400 pixel")

# Resize thành 800x600
resized_800x600 = cv2.resize(image_color, (800, 600))
output_file_2 = "resized_800x600.jpg"
cv2.imwrite(output_file_2, resized_800x600)
print(f"\n2️⃣  Resize 800×600:")
print(f"    ✓ File: {output_file_2}")
print(f"    ✓ Shape: {resized_800x600.shape}")
print(f"    ✓ Size: {os.path.getsize(output_file_2) / 1024:.2f} KB")
print(f"    ✓ Kích thước: 800 × 600 pixel")

# Resize thành 640x480 (thêm 1 kích thước nữa)
resized_640x480 = cv2.resize(image_color, (640, 480))
output_file_3 = "resized_640x480.jpg"
cv2.imwrite(output_file_3, resized_640x480)
print(f"\n3️⃣  Resize 640×480 (thêm):")
print(f"    ✓ File: {output_file_3}")
print(f"    ✓ Shape: {resized_640x480.shape}")
print(f"    ✓ Size: {os.path.getsize(output_file_3) / 1024:.2f} KB")
print(f"    ✓ Kích thước: 640 × 480 pixel")

# ============================================================================
# BƯỚC 6: CẮT ẢNH (CROP)
# ============================================================================

print("\n" + "=" * 80)
print("BƯỚC 6: CẮT ẢNH (CROP)")
print("=" * 80)

print("\n✂️  Cắt vùng ảnh:")
print("-" * 80)
print("Cú pháp: image[y1:y2, x1:x2]")

# Cắt vùng từ tọa độ (50,50) với kích thước 200×200
# Tọa độ: (x, y) = (50, 50)
# Kích thước: 200x200
# Cú pháp: image[y:y+height, x:x+width]
x1, y1, w1, h1 = 50, 50, 200, 200
cropped_200x200 = image_color[y1 : y1 + h1, x1 : x1 + w1]
crop_output_1 = "cropped_200x200.jpg"
cv2.imwrite(crop_output_1, cropped_200x200)

print(f"\n1️⃣  Cắt từ tọa độ (50, 50) kích thước 200×200:")
print(f"    ✓ File: {crop_output_1}")
print(f"    ✓ Vùng cắt: image[50:250, 50:250]")
print(f"    ✓ Shape: {cropped_200x200.shape}")
print(f"    ✓ Kích thước: {w1} × {h1} pixel")
print(f"    ✓ Size: {os.path.getsize(crop_output_1) / 1024:.2f} KB")

# Cắt vùng từ tọa độ (100,100) với kích thước 150×150
x2, y2, w2, h2 = 100, 100, 150, 150
cropped_150x150 = image_color[y2 : y2 + h2, x2 : x2 + w2]
crop_output_2 = "cropped_150x150.jpg"
cv2.imwrite(crop_output_2, cropped_150x150)

print(f"\n2️⃣  Cắt từ tọa độ (100, 100) kích thước 150×150:")
print(f"    ✓ File: {crop_output_2}")
print(f"    ✓ Vùng cắt: image[100:250, 100:250]")
print(f"    ✓ Shape: {cropped_150x150.shape}")
print(f"    ✓ Kích thước: {w2} × {h2} pixel")
print(f"    ✓ Size: {os.path.getsize(crop_output_2) / 1024:.2f} KB")

# Cắt thêm 1 vùng nữa: từ tọa độ (200,150) với kích thước 250×200
x3, y3, w3, h3 = 200, 150, 250, 200
cropped_250x200 = image_color[y3 : y3 + h3, x3 : x3 + w3]
crop_output_3 = "cropped_250x200.jpg"
cv2.imwrite(crop_output_3, cropped_250x200)

print(f"\n3️⃣  Cắt từ tọa độ (200, 150) kích thước 250×200 (thêm):")
print(f"    ✓ File: {crop_output_3}")
print(f"    ✓ Vùng cắt: image[150:350, 200:450]")
print(f"    ✓ Shape: {cropped_250x200.shape}")
print(f"    ✓ Kích thước: {w3} × {h3} pixel")
print(f"    ✓ Size: {os.path.getsize(crop_output_3) / 1024:.2f} KB")

# ============================================================================
# BƯỚC 7: TÓMLƯỢC THÔNG TIN
# ============================================================================

print("\n" + "=" * 80)
print("BƯỚC 7: TÓM LƯỢC THÔNG TIN FILE")
print("=" * 80)

print("\n📁 TÓMLƯỢC CÁC FILE OUTPUT:")
print("-" * 80)

resize_files = [
    (output_file_1, "Resize 300×400"),
    (output_file_2, "Resize 800×600"),
    (output_file_3, "Resize 640×480"),
]

crop_files = [
    (crop_output_1, "Crop 200×200 từ (50,50)"),
    (crop_output_2, "Crop 150×150 từ (100,100)"),
    (crop_output_3, "Crop 250×200 từ (200,150)"),
]

print("\n📐 CÁC ẢNH ĐÃ RESIZE:")
for fname, desc in resize_files:
    if os.path.exists(fname):
        img = cv2.imread(fname)
        h, w = img.shape[:2]
        print(
            f"  • {fname:<20} | {desc:<25} | {w}×{h} | {os.path.getsize(fname)/1024:>7.2f} KB"
        )

print("\n✂️  CÁC ẢNH ĐÃ CẮT:")
for fname, desc in crop_files:
    if os.path.exists(fname):
        img = cv2.imread(fname)
        h, w = img.shape[:2]
        print(
            f"  • {fname:<20} | {desc:<25} | {w}×{h} | {os.path.getsize(fname)/1024:>7.2f} KB"
        )

# ============================================================================
# BƯỚC 8: THỐNG KÊ TỔNG HỢP
# ============================================================================

print("\n" + "=" * 80)
print("BƯỚC 8: THỐNG KÊ TỔNG HỢP")
print("=" * 80)

print("\n📊 THÔNG TIN CHI TIẾT:")
print("-" * 80)

print("\n✓ Ảnh gốc (photo.jpg):")
print(f"  - Kích thước: {color_width} × {color_height} pixel")
print(f"  - Số chiều: {image_color.ndim} (3D array)")
print(f"  - Kênh màu: {color_channels} (BGR: Blue, Green, Red)")
print(f"  - Data type: {image_color.dtype}")
print(f"  - Size: {os.path.getsize('photo.jpg') / 1024:.2f} KB")

print("\n✓ Ảnh xám:")
print(f"  - Kích thước: {gray_width} × {gray_height} pixel")
print(f"  - Số chiều: {image_gray.ndim} (2D array)")
print(f"  - Kênh màu: 1 (Grayscale)")
print(f"  - Data type: {image_gray.dtype}")

print("\n✓ Các file đã tạo:")
all_files = resize_files + crop_files
total_size = sum(
    os.path.getsize(f[0]) / 1024 for f in all_files if os.path.exists(f[0])
)
print(f"  - Tổng số file: {len([f for f in all_files if os.path.exists(f[0])])}")
print(f"  - Tổng dung lượng: {total_size:.2f} KB")

# Danh sách file
output_files_list = [f[0] for f in resize_files + crop_files if os.path.exists(f[0])]
print(f"\n  Danh sách files: {', '.join(output_files_list)}")
