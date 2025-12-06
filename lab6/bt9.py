import cv2
import numpy as np
import os

print("=" * 80)
print("BÀI TẬP 9: VẼ CÁC HÌNH VẼ VÀ TEXT TRÊN ẢNH")
print("=" * 80)

# ============================================================================
# BƯỚC 1: CHUẨN BỊ ẢNH
# ============================================================================

print("\n" + "=" * 80)
print("BƯỚC 1: CHUẨN BỊ ẢNH")
print("=" * 80)

# Tạo ảnh trắng kích thước 600x500 (3 kênh BGR)
image_width = 600
image_height = 500
image = np.ones((image_height, image_width, 3), dtype=np.uint8) * 255

print(f"\n✓ Tạo ảnh trắng")
print(f"  - Kích thước: {image_width} × {image_height}")
print(f"  - Shape: {image.shape}")
print(f"  - Màu: Trắng (255, 255, 255)")

# Định nghĩa các màu sắc (BGR format trong OpenCV)
colors = {
    "Xanh dương": (255, 0, 0),  # Blue
    "Xanh lá": (0, 255, 0),  # Green
    "Đỏ": (0, 0, 255),  # Red
    "Vàng": (0, 255, 255),  # Yellow (Green + Red)
    "Tím": (255, 0, 255),  # Magenta (Blue + Red)
    "Cyan": (255, 255, 0),  # Cyan (Green + Blue)
    "Trắng": (255, 255, 255),  # White
    "Đen": (0, 0, 0),  # Black
}

# ============================================================================
# BƯỚC 2: VẼ CÁC HÌNH DẠNG
# ============================================================================

print("\n" + "=" * 80)
print("BƯỚC 2: VẼ CÁC HÌNH DẠNG")
print("=" * 80)

print("\n📐 Vẽ các hình khác nhau:")
print("-" * 80)

# 1. Vẽ đường thẳng
print("\n1️⃣  Đường thẳng")
pt1 = (0, 0)
pt2 = (400, 300)
color_line = colors["Xanh dương"]
thickness_line = 3
cv2.line(image, pt1, pt2, color_line, thickness_line)
print(f"    ✓ Từ {pt1} đến {pt2}")
print(f"    ✓ Màu: Xanh dương (BGR: {color_line})")
print(f"    ✓ Độ dày: {thickness_line} pixel")

# 2. Vẽ hình chữ nhật
print("\n2️⃣  Hình chữ nhật")
rect_pt1 = (50, 50)
rect_pt2 = (250, 200)
color_rect = colors["Đỏ"]
thickness_rect = 2
cv2.rectangle(image, rect_pt1, rect_pt2, color_rect, thickness_rect)
print(f"    ✓ Từ {rect_pt1} đến {rect_pt2}")
print(f"    ✓ Màu: Đỏ (BGR: {color_rect})")
print(f"    ✓ Độ dày: {thickness_rect} pixel")

# 3. Vẽ hình tròn
print("\n3️⃣  Hình tròn")
circle_center = (300, 150)
circle_radius = 80
color_circle = colors["Xanh lá"]
thickness_circle = 2
cv2.circle(image, circle_center, circle_radius, color_circle, thickness_circle)
print(f"    ✓ Tâm: {circle_center}")
print(f"    ✓ Bán kính: {circle_radius} pixel")
print(f"    ✓ Màu: Xanh lá (BGR: {color_circle})")
print(f"    ✓ Độ dày: {thickness_circle} pixel")

# 4. Vẽ hình ellipse
print("\n4️⃣  Hình ellipse")
ellipse_center = (200, 250)
ellipse_axes = (100, 50)
angle = 0
color_ellipse = colors["Vàng"]
thickness_ellipse = 2
cv2.ellipse(
    image, ellipse_center, ellipse_axes, angle, 0, 360, color_ellipse, thickness_ellipse
)
print(f"    ✓ Tâm: {ellipse_center}")
print(f"    ✓ Kích thước trục: {ellipse_axes}")
print(f"    ✓ Góc: {angle}°")
print(f"    ✓ Màu: Vàng (BGR: {color_ellipse})")
print(f"    ✓ Độ dày: {thickness_ellipse} pixel")

# 5. Vẽ đa giác (polygon)
print("\n5️⃣  Đa giác (Polygon/Triangle)")
polygon_points = np.array([(50, 100), (150, 50), (200, 150)], dtype=np.int32)
color_polygon = colors["Tím"]
thickness_polygon = 2
cv2.polylines(image, [polygon_points], True, color_polygon, thickness_polygon)
print(f"    ✓ Các đỉnh: {polygon_points.tolist()}")
print(f"    ✓ Hình dạng: Tam giác")
print(f"    ✓ Màu: Tím (BGR: {color_polygon})")
print(f"    ✓ Độ dày: {thickness_polygon} pixel")

# ============================================================================
# BƯỚC 3: VIẾT TEXT TRÊN ẢNH
# ============================================================================

print("\n" + "=" * 80)
print("BƯỚC 3: VIẾT TEXT TRÊN ẢNH")
print("=" * 80)

print("\n📝 Viết text:")
print("-" * 80)

# Định nghĩa font
font = cv2.FONT_HERSHEY_SIMPLEX

# 1. Viết text "Python Programming"
print("\n1️⃣  Text 'Python Programming'")
text1 = "Python Programming"
text1_position = (50, 50)
text1_color = colors["Trắng"]
text1_scale = 1.5
text1_thickness = 2
cv2.putText(
    image, text1, text1_position, font, text1_scale, text1_color, text1_thickness
)
print(f"    ✓ Nội dung: '{text1}'")
print(f"    ✓ Vị trí: {text1_position}")
print(f"    ✓ Màu: Trắng (BGR: {text1_color})")
print(f"    ✓ Kích thước: {text1_scale}")
print(f"    ✓ Độ dày: {text1_thickness} pixel")

# 2. Viết text "Image Processing"
print("\n2️⃣  Text 'Image Processing'")
text2 = "Image Processing"
text2_position = (50, 100)
text2_color = colors["Đen"]
text2_scale = 1.0
text2_thickness = 2
cv2.putText(
    image, text2, text2_position, font, text2_scale, text2_color, text2_thickness
)
print(f"    ✓ Nội dung: '{text2}'")
print(f"    ✓ Vị trí: {text2_position}")
print(f"    ✓ Màu: Đen (BGR: {text2_color})")
print(f"    ✓ Kích thước: {text2_scale}")
print(f"    ✓ Độ dày: {text2_thickness} pixel")

# 3. Thêm các text bổ sung để làm đẹp
print("\n3️⃣  Text bổ sung (tùy chọn)")
text3 = "OpenCV Drawing Demo"
text3_position = (150, 450)
text3_color = colors["Cyan"]
text3_scale = 1.0
text3_thickness = 2
cv2.putText(
    image, text3, text3_position, font, text3_scale, text3_color, text3_thickness
)
print(f"    ✓ Nội dung: '{text3}'")
print(f"    ✓ Vị trí: {text3_position}")
print(f"    ✓ Màu: Cyan (BGR: {text3_color})")
print(f"    ✓ Kích thước: {text3_scale}")

# ============================================================================
# BƯỚC 4: THÊM CHÚ THÍCH HÌNH VẼ
# ============================================================================

print("\n" + "=" * 80)
print("BƯỚC 4: THÊM CHÚ THÍCH")
print("=" * 80)

print("\n📌 Thêm nhãn cho các hình:")
print("-" * 80)

# Nhãn cho các hình
annotations = [
    ("Line", (210, 155), colors["Xanh dương"]),
    ("Rectangle", (100, 30), colors["Đỏ"]),
    ("Circle", (310, 80), colors["Xanh lá"]),
    ("Ellipse", (100, 320), colors["Vàng"]),
    ("Polygon", (80, 120), colors["Tím"]),
]

for label, position, color in annotations:
    cv2.putText(image, label, position, cv2.FONT_HERSHEY_TRIPLEX, 0.6, color, 1)
    print(f"    ✓ {label:<10} tại {position}")

# ============================================================================
# BƯỚC 5: LƯU ẢNH ĐÃ VẼ
# ============================================================================

print("\n" + "=" * 80)
print("BƯỚC 5: LƯU ẢNH ĐÃ VẼ")
print("=" * 80)

# Lưu ảnh chính
main_output = "drawn_shapes.jpg"
cv2.imwrite(main_output, image)
print(f"\n✓ Lưu ảnh chính: {main_output}")
print(f"  - Size: {os.path.getsize(main_output) / 1024:.2f} KB")
print(f"  - Kích thước: {image.shape[1]} × {image.shape[0]}")

# Tạo các phiên bản khác nhau

# 1. Ảnh chỉ có hình dạng (không có text)
print("\n📌 Tạo các phiên bản khác:")
print("-" * 80)

image_shapes_only = np.ones((image_height, image_width, 3), dtype=np.uint8) * 255

# Vẽ lại các hình
cv2.line(image_shapes_only, pt1, pt2, color_line, thickness_line)
cv2.rectangle(image_shapes_only, rect_pt1, rect_pt2, color_rect, thickness_rect)
cv2.circle(
    image_shapes_only, circle_center, circle_radius, color_circle, thickness_circle
)
cv2.ellipse(
    image_shapes_only,
    ellipse_center,
    ellipse_axes,
    angle,
    0,
    360,
    color_ellipse,
    thickness_ellipse,
)
cv2.polylines(
    image_shapes_only, [polygon_points], True, color_polygon, thickness_polygon
)

shapes_output = "drawn_shapes_only.jpg"
cv2.imwrite(shapes_output, image_shapes_only)
print(f"\n1️⃣  Ảnh chỉ hình dạng: {shapes_output}")
print(f"    Size: {os.path.getsize(shapes_output) / 1024:.2f} KB")

# 2. Ảnh chỉ có text
print("\n2️⃣  Ảnh chỉ text: drawn_text_only.jpg")
image_text_only = np.ones((image_height, image_width, 3), dtype=np.uint8) * 255
cv2.putText(
    image_text_only,
    text1,
    text1_position,
    font,
    text1_scale,
    text1_color,
    text1_thickness,
)
cv2.putText(
    image_text_only,
    text2,
    text2_position,
    font,
    text2_scale,
    text2_color,
    text2_thickness,
)
cv2.putText(
    image_text_only,
    text3,
    text3_position,
    font,
    text3_scale,
    text3_color,
    text3_thickness,
)

text_output = "drawn_text_only.jpg"
cv2.imwrite(text_output, image_text_only)
print(f"    Size: {os.path.getsize(text_output) / 1024:.2f} KB")

# 3. Ảnh với nền gradient
print("\n3️⃣  Ảnh với nền gradient: drawn_shapes_gradient.jpg")
image_gradient = np.zeros((image_height, image_width, 3), dtype=np.uint8)

# Tạo gradient nền
for i in range(image_height):
    image_gradient[i, :] = [
        int(255 * i / image_height),
        150,
        200 - int(150 * i / image_height),
    ]

# Vẽ lại các hình
cv2.line(image_gradient, pt1, pt2, color_line, thickness_line)
cv2.rectangle(image_gradient, rect_pt1, rect_pt2, color_rect, thickness_rect)
cv2.circle(image_gradient, circle_center, circle_radius, color_circle, thickness_circle)
cv2.ellipse(
    image_gradient,
    ellipse_center,
    ellipse_axes,
    angle,
    0,
    360,
    color_ellipse,
    thickness_ellipse,
)
cv2.polylines(image_gradient, [polygon_points], True, color_polygon, thickness_polygon)
cv2.putText(
    image_gradient,
    text1,
    text1_position,
    font,
    text1_scale,
    text1_color,
    text1_thickness,
)
cv2.putText(
    image_gradient,
    text2,
    text2_position,
    font,
    text2_scale,
    text2_color,
    text2_thickness,
)

gradient_output = "drawn_shapes_gradient.jpg"
cv2.imwrite(gradient_output, image_gradient)
print(f"    Size: {os.path.getsize(gradient_output) / 1024:.2f} KB")

# ============================================================================
# BƯỚC 6: THỐNG KÊ THÔNG TIN VỀ CÁC HÌNH VẼ
# ============================================================================

print("\n" + "=" * 80)
print("BƯỚC 6: THỐNG KÊ THÔNG TIN")
print("=" * 80)

print("\n📊 BẢNG TỔNG KẾT CÁC HÌNH VẼ:")
print("-" * 80)
print(f"{'Hình dạng':<15} {'Tham số':<30} {'Màu':<15} {'Độ dày'}")
print("-" * 80)

shapes_info = [
    (
        "Đường thẳng",
        f"({pt1[0]},{pt1[1]}) → ({pt2[0]},{pt2[1]})",
        "Xanh dương",
        thickness_line,
    ),
    (
        "Chữ nhật",
        f"({rect_pt1[0]},{rect_pt1[1]}) → ({rect_pt2[0]},{rect_pt2[1]})",
        "Đỏ",
        thickness_rect,
    ),
    (
        "Tròn",
        f"C({circle_center[0]},{circle_center[1]}), R={circle_radius}",
        "Xanh lá",
        thickness_circle,
    ),
    (
        "Ellipse",
        f"C({ellipse_center[0]},{ellipse_center[1]}), A={ellipse_axes}",
        "Vàng",
        thickness_ellipse,
    ),
    ("Đa giác", "3 đỉnh (tam giác)", "Tím", thickness_polygon),
]

for shape, param, color, thick in shapes_info:
    print(f"{shape:<15} {param:<30} {color:<15} {thick}")

print("\n📝 BẢNG TỔNG KẾT TEXT:")
print("-" * 80)
print(f"{'Nội dung':<20} {'Vị trí':<20} {'Màu':<15} {'Kích thước':<12} {'Độ dày'}")
print("-" * 80)

texts_info = [
    (text1, text1_position, "Trắng", text1_scale, text1_thickness),
    (text2, text2_position, "Đen", text2_scale, text2_thickness),
    (text3, text3_position, "Cyan", text3_scale, text3_thickness),
]

for text, pos, color, scale, thick in texts_info:
    print(f"{text:<20} {str(pos):<20} {color:<15} {scale:<12} {thick}")

# ============================================================================
# BƯỚC 7: THÔNG TIN CHI TIẾT VỀ CÁC HÀM OPENCV
# ============================================================================

print("\n" + "=" * 80)
print("BƯỚC 7: THÔNG TIN CHI TIẾT VỀ CÁC HÀM OPENCV")
print("=" * 80)

functions_info = {
    "cv2.line()": """
    Vẽ đường thẳng giữa hai điểm
    cv2.line(image, pt1, pt2, color, thickness)
    - pt1, pt2: Tọa độ (x, y)
    - color: Màu sắc (B, G, R)
    - thickness: Độ dày (pixel), -1 để tô đặc
    """,
    "cv2.rectangle()": """
    Vẽ hình chữ nhật
    cv2.rectangle(image, pt1, pt2, color, thickness)
    - pt1: Góc trên bên trái
    - pt2: Góc dưới bên phải
    - thickness: -1 để tô đặc
    """,
    "cv2.circle()": """
    Vẽ hình tròn
    cv2.circle(image, center, radius, color, thickness)
    - center: Tọa độ tâm (x, y)
    - radius: Bán kính (pixel)
    - thickness: -1 để tô đặc
    """,
    "cv2.ellipse()": """
    Vẽ hình ellipse
    cv2.ellipse(image, center, axes, angle, startAngle, endAngle, color, thickness)
    - axes: (major_axis, minor_axis)
    - angle: Góc xoay
    - startAngle, endAngle: Góc bắt đầu và kết thúc
    """,
    "cv2.polylines()": """
    Vẽ đa giác (polygon)
    cv2.polylines(image, pts, isClosed, color, thickness)
    - pts: Danh sách điểm [[x1,y1], [x2,y2], ...]
    - isClosed: True/False - đóng hình hay không
    """,
    "cv2.putText()": """
    Viết text trên ảnh
    cv2.putText(image, text, org, fontFace, fontScale, color, thickness)
    - org: Vị trí bắt đầu (x, y)
    - fontFace: Loại font (FONT_HERSHEY_SIMPLEX, ...)
    - fontScale: Kích thước font
    - color: Màu sắc (B, G, R)
    """,
}

for func_name, func_desc in functions_info.items():
    print(f"\n{func_name}:")
    print(func_desc)

# ============================================================================
# BƯỚC 8: TÓM LƯỢC KẾT QUẢ
# ============================================================================

print("\n" + "=" * 80)
print("BƯỚC 8: TÓM LƯỢC KẾT QUẢ")
print("=" * 80)

output_files = [main_output, shapes_output, text_output, gradient_output]

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

print("\n📋 CÁC HÌNH DẠNG VẼ:")
print("-" * 80)
print(f"  • Đường thẳng: 1 đường")
print(f"  • Hình chữ nhật: 1 hình")
print(f"  • Hình tròn: 1 hình")
print(f"  • Hình ellipse: 1 hình")
print(f"  • Đa giác: 1 tam giác")
print(f"  • Text: 3 dòng")
print(f"  • Nhãn: 5 nhãn")

print("\n🎨 TỔNG CỘNG: 18 phần tử vẽ")

print("\n" + "=" * 80)
print("✅ BÀI TẬP 9 HOÀN THÀNH")
print("=" * 80)
print(f"\nFile chính: {main_output}")
