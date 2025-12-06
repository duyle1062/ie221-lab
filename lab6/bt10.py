import cv2
import numpy as np
import os

print("=" * 80)
print("BÀI TẬP 10: TẢI, PHÁT VÀ TRÍCH XUẤT THÔNG TIN VIDEO")
print("=" * 80)

# ============================================================================
# BƯỚC 0: CHUẨN BỊ FILE VIDEO
# ============================================================================

print("\n" + "=" * 80)
print("BƯỚC 0: CHUẨN BỊ FILE VIDEO")
print("=" * 80)

video_file = "sample_video.mp4"

if not os.path.exists(video_file):
    print(f"\n📝 Tạo file video test: {video_file}")
    print("   (Vì file video chưa tồn tại)")

    # Thông số video
    frame_width = 640
    frame_height = 480
    fps = 20
    duration = 5  # 5 giây
    total_frames = int(fps * duration)

    # Tạo video writer
    fourcc = cv2.VideoWriter_fourcc(*"mp4v")
    out = cv2.VideoWriter(video_file, fourcc, fps, (frame_width, frame_height))

    # Tạo các frame khác nhau
    for frame_num in range(total_frames):
        # Tạo ảnh với màu gradient
        frame = np.zeros((frame_height, frame_width, 3), dtype=np.uint8)

        # Gradient nền
        for y in range(frame_height):
            for x in range(frame_width):
                frame[y, x] = [
                    int(255 * frame_num / total_frames),
                    int(128 + 127 * np.sin(frame_num / total_frames * np.pi)),
                    int(200 - 100 * frame_num / total_frames),
                ]

        # Vẽ các hình
        cv2.circle(
            frame, (320, 240), 50 + int(30 * np.sin(frame_num / 10)), (0, 255, 255), 2
        )
        cv2.rectangle(frame, (100, 100), (540, 380), (255, 0, 0), 2)

        # Viết frame number
        cv2.putText(
            frame,
            f"Frame {frame_num + 1}/{total_frames}",
            (20, 40),
            cv2.FONT_HERSHEY_SIMPLEX,
            1.0,
            (255, 255, 255),
            2,
        )
        cv2.putText(
            frame,
            f"Time: {frame_num / fps:.2f}s",
            (20, 80),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.8,
            (200, 200, 200),
            1,
        )

        out.write(frame)

    out.release()
    print(f"   ✓ Tạo video thành công")
    print(f"     - Độ phân giải: {frame_width} × {frame_height}")
    print(f"     - FPS: {fps}")
    print(f"     - Thời lượng: {duration} giây ({total_frames} frame)")
    print(f"     - File size: {os.path.getsize(video_file) / 1024:.2f} KB")
else:
    print(f"\n✓ File video đã tồn tại: {video_file}")
    print(f"  File size: {os.path.getsize(video_file) / 1024:.2f} KB")

# ============================================================================
# BƯỚC 1: TẢI VÀ MỞ FILE VIDEO
# ============================================================================

print("\n" + "=" * 80)
print("BƯỚC 1: TẢI VÀ MỞ FILE VIDEO")
print("=" * 80)

# Tạo VideoCapture object
cap = cv2.VideoCapture(video_file)

# Kiểm tra xem video đã được mở thành công
if not cap.isOpened():
    print(f"\n❌ Lỗi: Không thể mở file video: {video_file}")
    exit(1)

print(f"\n✓ Đã mở file video: {video_file}")

# ============================================================================
# BƯỚC 2: LẤY THÔNG TIN VIDEO
# ============================================================================

print("\n" + "=" * 80)
print("BƯỚC 2: LẤY THÔNG TIN VIDEO")
print("=" * 80)

# Lấy các thuộc tính video
frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = int(cap.get(cv2.CAP_PROP_FPS))
total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
duration = total_frames / fps if fps > 0 else 0

print("\n📊 THÔNG TIN VIDEO:")
print("-" * 80)
print(f"1. Tên file: {video_file}")
print(f"2. Độ phân giải:")
print(f"   - Width (chiều rộng): {frame_width} pixel")
print(f"   - Height (chiều cao): {frame_height} pixel")
print(f"   - Định dạng: {frame_width} × {frame_height}")
print(f"3. FPS (Frames Per Second): {fps}")
print(f"4. Tổng số frame: {total_frames}")
print(f"5. Thời lượng video: {duration:.2f} giây")
print(f"6. File size: {os.path.getsize(video_file) / (1024 * 1024):.2f} MB")

# ============================================================================
# BƯỚC 3: PHÁT VIDEO
# ============================================================================

print("\n" + "=" * 80)
print("BƯỚC 3: PHÁT VIDEO")
print("=" * 80)

print("\n▶️  Đang phát video...")
print("-" * 80)

frame_count = 0
extracted_frames = []

# Phát video toàn bộ
while True:
    ret, frame = cap.read()

    if not ret:
        break  # Kết thúc video

    frame_count += 1

    # In tiến độ (mỗi 5 frame)
    if frame_count % 5 == 0 or frame_count == 1:
        print(
            f"  Phát frame {frame_count}/{total_frames} ({frame_count/total_frames*100:.1f}%)"
        )

    # Lưu 5 frame đầu tiên để trích xuất sau
    if frame_count <= 5:
        extracted_frames.append(frame.copy())

    # Thử hiển thị video (nếu có GUI)
    try:
        cv2.imshow("Video Player", frame)
        # Nhấn 'q' để dừng
        if cv2.waitKey(int(1000 / fps)) & 0xFF == ord("q"):
            print("  ⏹️  Dừng phát (nhấn q)")
            break
    except:
        pass  # Không có GUI

# Đóng cửa sổ hiển thị
try:
    cv2.destroyAllWindows()
except:
    pass

print(f"✓ Phát video xong")
print(f"  Tổng frame đã phát: {frame_count}")

# ============================================================================
# BƯỚC 4: ĐẾM VÀ THỐNG KÊ TỔNG SỐ FRAME
# ============================================================================

print("\n" + "=" * 80)
print("BƯỚC 4: ĐẾM VÀ THỐNG KÊ TỔNG SỐ FRAME")
print("=" * 80)

print("\n📈 THỐNG KÊ FRAME:")
print("-" * 80)
print(f"1. Tổng số frame từ thông tin video: {total_frames}")
print(f"2. Số frame đã phát: {frame_count}")
print(f"3. Kiểm tra: {'✓ Khớp' if frame_count == total_frames else '⚠️ Không khớp'}")
print(f"4. Thời lượng video: {duration:.2f} giây")
print(f"5. Tốc độ: {fps} FPS")
print(f"6. Tổng số mili-giây: {duration * 1000:.0f} ms")

# ============================================================================
# BƯỚC 5: LƯU THÔNG TIN VIDEO VÀO FILE TEXT
# ============================================================================

print("\n" + "=" * 80)
print("BƯỚC 5: LƯU THÔNG TIN VIDEO VÀO FILE TEXT")
print("=" * 80)

info_file = "video_info.txt"

with open(info_file, "w", encoding="utf-8") as f:
    f.write("=" * 80 + "\n")
    f.write("THÔNG TIN VIDEO\n")
    f.write("=" * 80 + "\n\n")

    f.write("1. THÔNG TIN CƠ BẢN:\n")
    f.write("-" * 80 + "\n")
    f.write(f"Tên file: {video_file}\n")
    f.write(f"Đường dẫn: {os.path.abspath(video_file)}\n")
    f.write(f"File size: {os.path.getsize(video_file) / (1024 * 1024):.2f} MB\n")
    f.write(
        f"Ngày tạo: {__import__('datetime').datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n"
    )

    f.write("2. THÔNG TIN KỸ THUẬT:\n")
    f.write("-" * 80 + "\n")
    f.write(f"Độ phân giải (Resolution):\n")
    f.write(f"  - Width: {frame_width} pixel\n")
    f.write(f"  - Height: {frame_height} pixel\n")
    f.write(f"  - Format: {frame_width} × {frame_height}\n")
    f.write(f"  - Aspect Ratio: {frame_width/frame_height:.2f}:1\n\n")

    f.write(f"FPS (Frames Per Second): {fps}\n")
    f.write(f"Tổng số frame: {total_frames}\n")
    f.write(
        f"Thời lượng video: {duration:.2f} giây ({int(duration//60)} phút {duration%60:.0f} giây)\n"
    )
    f.write(f"Tổng mili-giây: {duration * 1000:.0f} ms\n\n")

    f.write("3. TÍNH TOÁN:\n")
    f.write("-" * 80 + "\n")
    f.write(
        f"Bitrate (ước tính): {(os.path.getsize(video_file) / (1024 * 1024)) / duration * 8:.2f} Mbps\n"
    )
    f.write(f"Frame duration: {1000 / fps:.2f} ms\n")
    f.write(f"Pixel count per frame: {frame_width * frame_height:,}\n")
    f.write(f"Total pixel count: {frame_width * frame_height * total_frames:,}\n\n")

    f.write("4. CÁC FILE TRÍCH XUẤT:\n")
    f.write("-" * 80 + "\n")
    f.write(f"Số frame được trích xuất: {len(extracted_frames)}\n")
    for i in range(1, len(extracted_frames) + 1):
        f.write(f"  - frame_{i:02d}.jpg\n")
    f.write("\n")

    f.write("=" * 80 + "\n")
    f.write("Tạo bởi: Exercise 10 - Video Processing\n")
    f.write("=" * 80 + "\n")

print(f"\n✓ Lưu thông tin vào: {info_file}")
print(f"  File size: {os.path.getsize(info_file) / 1024:.2f} KB")

# Hiển thị nội dung
print("\nNội dung file info:")
print("-" * 80)
with open(info_file, "r", encoding="utf-8") as f:
    print(f.read())

# ============================================================================
# BƯỚC 6: TRÍCH XUẤT 5 FRAME ĐẦU TIÊN
# ============================================================================

print("\n" + "=" * 80)
print("BƯỚC 6: TRÍCH XUẤT 5 FRAME ĐẦU TIÊN")
print("=" * 80)

print(f"\n🎬 Lưu {len(extracted_frames)} frame đầu tiên:")
print("-" * 80)

for i, frame in enumerate(extracted_frames, 1):
    output_filename = f"frame_{i:02d}.jpg"
    cv2.imwrite(output_filename, frame)
    print(f"  {i}. {output_filename}")
    print(f"     - Size: {frame.shape[1]} × {frame.shape[0]}")
    print(f"     - File size: {os.path.getsize(output_filename) / 1024:.2f} KB")

# ============================================================================
# BƯỚC 7: THÔNG TIN CHI TIẾT VỀ CÁC HÀM
# ============================================================================

print("\n" + "=" * 80)
print("BƯỚC 7: THÔNG TIN CHI TIẾT VỀ CÁC HÀM OPENCV")
print("=" * 80)

functions_info = """
📖 cv2.VideoCapture(filename)
   Mở file video để xử lý
   Parameters:
   - filename: Đường dẫn file video (mp4, avi, mov, v.v.)
   
   Ví dụ: cap = cv2.VideoCapture('video.mp4')

📖 cap.get(propId)
   Lấy thuộc tính của video
   Các thuộc tính thường dùng:
   - cv2.CAP_PROP_FRAME_WIDTH: Chiều rộng frame
   - cv2.CAP_PROP_FRAME_HEIGHT: Chiều cao frame
   - cv2.CAP_PROP_FPS: Số frame trên giây
   - cv2.CAP_PROP_FRAME_COUNT: Tổng số frame
   - cv2.CAP_PROP_FOURCC: Mã codec
   
   Ví dụ: fps = int(cap.get(cv2.CAP_PROP_FPS))

📖 cap.read()
   Đọc frame tiếp theo từ video
   Return:
   - ret: Boolean - True nếu frame được đọc thành công
   - frame: Ảnh frame (numpy array)
   
   Ví dụ:
   ret, frame = cap.read()
   if not ret:
       print("Hết video")

📖 cap.set(propId, value)
   Thiết lập thuộc tính của video
   
   Ví dụ:
   cap.set(cv2.CAP_PROP_POS_FRAMES, 100)  # Đến frame 100
   cap.set(cv2.CAP_PROP_POS_MSEC, 5000)   # Đến 5 giây

📖 cap.release()
   Đóng file video
   
   Ví dụ: cap.release()
"""

print(functions_info)

# ============================================================================
# BƯỚC 8: TÓM LƯỢC KẾT QUẢ
# ============================================================================

print("\n" + "=" * 80)
print("BƯỚC 8: TÓM LƯỢC KẾT QUẢ")
print("=" * 80)

output_files = [info_file]
for i in range(1, len(extracted_frames) + 1):
    output_files.append(f"frame_{i:02d}.jpg")

print("\n📁 CÁC FILE ĐÃ TẠO:")
print("-" * 80)

total_size = 0
for fname in output_files:
    if os.path.exists(fname):
        size_kb = os.path.getsize(fname) / 1024
        total_size += size_kb
        file_type = "Video Info" if fname.endswith(".txt") else "Frame"
        print(f"  ✓ {fname:<20} ({file_type:<12}) {size_kb:>8.2f} KB")

print("-" * 80)
print(f"  📊 Tổng: {len(output_files)} file | Dung lượng: {total_size:.2f} KB")

print("\n📋 THỐNG KÊ VIDEO:")
print("-" * 80)
print(f"  • Video file: {video_file}")
print(f"  • Độ phân giải: {frame_width} × {frame_height}")
print(f"  • FPS: {fps}")
print(f"  • Tổng frame: {total_frames}")
print(f"  • Thời lượng: {duration:.2f} giây")
print(f"  • Frame trích xuất: {len(extracted_frames)}")

# Đóng VideoCapture
cap.release()

print("\n" + "=" * 80)
print("✅ BÀI TẬP 10 HOÀN THÀNH")
print("=" * 80)
print(f"\nThông tin video: {info_file}")
print(f"Frame trích xuất: frame_01.jpg - frame_{len(extracted_frames):02d}.jpg")
