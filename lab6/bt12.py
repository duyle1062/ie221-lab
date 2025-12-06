import os
import cv2
import numpy as np
import subprocess
import json

print("=" * 80)
print("BÀI TẬP 12: CẮT VIDEO THÀNH CÁC ĐOẠN NHỎ VÀ TÁCH ÂM THANH")
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

    # Thông số video
    frame_width = 640
    frame_height = 480
    fps = 20
    duration = 30  # 30 giây (để cắt thành 3 đoạn 10 giây)
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
            f"Time: {frame_num / fps:.1f}s",
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
    print(f"     - File size: {os.path.getsize(video_file) / (1024 * 1024):.2f} MB")
else:
    print(f"\n✓ File video đã tồn tại: {video_file}")
    print(f"  File size: {os.path.getsize(video_file) / (1024 * 1024):.2f} MB")

# ============================================================================
# BƯỚC 1: TẢI FILE VIDEO VÀ LẤY THÔNG TIN
# ============================================================================

print("\n" + "=" * 80)
print("BƯỚC 1: TẢI FILE VIDEO VÀ LẤY THÔNG TIN")
print("=" * 80)

print(f"\n📹 Tải file video: {video_file}")

# Sử dụng cv2.VideoCapture để lấy thông tin
cap = cv2.VideoCapture(video_file)

if not cap.isOpened():
    print(f"❌ Lỗi: Không thể mở file video: {video_file}")
    exit(1)

print("✓ Đã tải video thành công")

# ====================================================================
# BƯỚC 2: LẤY THÔNG TIN VIDEO
# ====================================================================

print("\n" + "=" * 80)
print("BƯỚC 2: LẤY THÔNG TIN VIDEO")
print("=" * 80)

# Lấy thông tin
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = int(cap.get(cv2.CAP_PROP_FPS))
total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
duration = total_frames / fps if fps > 0 else 0

print("\n📊 THÔNG TIN VIDEO:")
print("-" * 80)
print(f"1. Tên file: {video_file}")
print(f"2. Độ phân giải:")
print(f"   - Width: {width} pixel")
print(f"   - Height: {height} pixel")
print(f"   - Format: {width} × {height}")
print(f"3. Frame rate (FPS): {fps}")
print(
    f"4. Thời lượng: {duration:.2f} giây ({int(duration//60)} phút {duration%60:.0f} giây)"
)
print(f"5. Tổng số frame: {total_frames}")
print(f"6. File size: {os.path.getsize(video_file) / (1024 * 1024):.2f} MB")

# ====================================================================
# BƯỚC 3: CẮT VIDEO THÀNH CÁC ĐOẠN 10 GIÂY
# ====================================================================

print("\n" + "=" * 80)
print("BƯỚC 3: CẮT VIDEO THÀNH CÁC ĐOẠN 10 GIÂY")
print("=" * 80)

segment_duration = 10  # 10 giây mỗi đoạn
total_segments = int(np.ceil(duration / segment_duration))

print(f"\n✂️  Cắt video:")
print("-" * 80)
print(f"Thời lượng mỗi đoạn: {segment_duration} giây")
print(f"Tổng số đoạn: {total_segments}")
print(f"Thời lượng video: {duration:.2f} giây\n")

segment_files = []

for seg_num in range(total_segments):
    # Tính thời gian bắt đầu và kết thúc
    start_frame = seg_num * segment_duration * fps
    end_frame = min((seg_num + 1) * segment_duration * fps, total_frames)
    start_time = start_frame / fps
    end_time = end_frame / fps
    segment_length = end_time - start_time

    # Thiết lập frame bắt đầu
    cap.set(cv2.CAP_PROP_POS_FRAMES, start_frame)

    # Tên file output
    output_filename = f"video_segment_{seg_num+1:02d}.mp4"
    segment_files.append(output_filename)

    # Tạo VideoWriter cho segment
    fourcc = cv2.VideoWriter_fourcc(*"mp4v")
    out_segment = cv2.VideoWriter(output_filename, fourcc, fps, (width, height))

    # Đọc và ghi frame
    frame_count = 0
    while True:
        ret, frame = cap.read()
        if not ret or cap.get(cv2.CAP_PROP_POS_FRAMES) > end_frame:
            break
        out_segment.write(frame)
        frame_count += 1

    out_segment.release()

    file_size = (
        os.path.getsize(output_filename) / 1024
        if os.path.exists(output_filename)
        else 0
    )
    print(f"{seg_num+1}️⃣  Đoạn {seg_num+1}")
    print(f"    ✓ File: {output_filename}")
    print(
        f"    ✓ Thời gian: {start_time:.1f}s - {end_time:.1f}s ({segment_length:.1f}s)"
    )
    print(f"    ✓ Frame: {int(start_frame)} - {int(end_frame)}")
    print(f"    ✓ Kích thước: {file_size:.2f} KB")

cap.release()

# ====================================================================
# BƯỚC 4: TÁCH ÂM THANH TỪ VIDEO (NẾU CÓ)
# ====================================================================

print("\n" + "=" * 80)
print("BƯỚC 4: TÁCH ÂM THANH TỪ VIDEO")
print("=" * 80)

print("\n🔊 Trích xuất âm thanh:")
print("-" * 80)

try:
    # Sử dụng ffmpeg để trích âm thanh
    print("\n1️⃣  Lưu thành WAV")
    audio_wav = "extracted_audio.wav"

    cmd = f"ffmpeg -i {video_file} -q:a 9 -n {audio_wav} 2>&1"
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)

    if os.path.exists(audio_wav):
        wav_size = os.path.getsize(audio_wav) / 1024
        print(f"    ✓ File: {audio_wav}")
        print(f"    ✓ Kích thước: {wav_size:.2f} KB")
    else:
        print(f"    ⚠️  Không thể tách âm thanh")

    # Lưu thành MP3
    print(f"\n2️⃣  Lưu thành MP3")
    audio_mp3 = "extracted_audio.mp3"

    cmd = f"ffmpeg -i {video_file} -q:a 9 -n {audio_mp3} 2>&1"
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)

    if os.path.exists(audio_mp3):
        mp3_size = os.path.getsize(audio_mp3) / 1024
        print(f"    ✓ File: {audio_mp3}")
        print(f"    ✓ Kích thước: {mp3_size:.2f} KB")
    else:
        print(f"    ⚠️  Không thể tạo MP3")

    # Tách âm thanh từ các segment
    print(f"\n3️⃣  Tách âm thanh từ các segment:")
    print("-" * 80)

    for i, seg_file in enumerate(segment_files, 1):
        audio_file = f"segment_{i:02d}_audio.wav"
        cmd = f"ffmpeg -i {seg_file} -q:a 9 -n {audio_file} 2>&1"
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True)

        if os.path.exists(audio_file):
            size = os.path.getsize(audio_file) / 1024
            print(f"    ✓ Segment {i}: {audio_file} ({size:.2f} KB)")

except Exception as e:
    print(f"\n⚠️  Lỗi khi tách âm thanh: {str(e)}")
    print("   Đảm bảo ffmpeg đã được cài đặt")

# ====================================================================
# BƯỚC 5: THÔNG TIN CHI TIẾT VỀ CÁC HÀM
# ====================================================================

print("\n" + "=" * 80)
print("BƯỚC 5: THÔNG TIN CHI TIẾT VỀ CÁC HÀM OPENCV")
print("=" * 80)

functions_info = """
📖 cv2.VideoCapture(filename)
   Mở file video để xử lý
   
   Ví dụ: cap = cv2.VideoCapture('video.mp4')

📖 cap.get(propId)
   Lấy thuộc tính của video
   Các thuộc tính thường dùng:
   - cv2.CAP_PROP_FRAME_WIDTH: Chiều rộng frame
   - cv2.CAP_PROP_FRAME_HEIGHT: Chiều cao frame
   - cv2.CAP_PROP_FPS: Số frame trên giây
   - cv2.CAP_PROP_FRAME_COUNT: Tổng số frame
   
   Ví dụ: fps = int(cap.get(cv2.CAP_PROP_FPS))

📖 cap.set(propId, value)
   Thiết lập thuộc tính của video
   
   Ví dụ:
   cap.set(cv2.CAP_PROP_POS_FRAMES, 100)  # Đến frame 100
   cap.set(cv2.CAP_PROP_POS_MSEC, 5000)   # Đến 5 giây

📖 cap.read()
   Đọc frame tiếp theo từ video
   Return:
   - ret: Boolean - True nếu frame được đọc thành công
   - frame: Ảnh frame (numpy array)
   
   Ví dụ:
   ret, frame = cap.read()
   if not ret:
       print("Hết video")

📖 cv2.VideoWriter(filename, fourcc, fps, frameSize)
   Tạo writer để ghi video
   
   Ví dụ:
   fourcc = cv2.VideoWriter_fourcc(*'mp4v')
   out = cv2.VideoWriter('output.mp4', fourcc, fps, (width, height))
   out.write(frame)
   out.release()

📖 cap.release()
   Đóng file video
   
   Ví dụ: cap.release()

📖 ffmpeg Command Line
   Tách âm thanh từ video:
   ffmpeg -i input.mp4 -q:a 9 -n output.wav
   
   Tham số:
   - -i: Input file
   - -q:a: Quality (1-9, cao nhất là 9)
   - -n: Không hỏi nếu file tồn tại
"""

print(functions_info)

# ====================================================================
# BƯỚC 6: THỐNG KÊ THÔNG TIN
# ====================================================================

print("\n" + "=" * 80)
print("BƯỚC 6: THỐNG KÊ THÔNG TIN")
print("=" * 80)

# Thu thập tất cả các file output
output_files = segment_files.copy()

if os.path.exists("extracted_audio.wav"):
    output_files.append("extracted_audio.wav")
if os.path.exists("extracted_audio.mp3"):
    output_files.append("extracted_audio.mp3")

for i in range(1, total_segments + 1):
    audio_file = f"segment_{i:02d}_audio.wav"
    if os.path.exists(audio_file):
        output_files.append(audio_file)

print("\n📁 CÁC FILE ĐÃ TẠO:")
print("-" * 80)

total_size = 0

print("\n📹 File Video:")
for fname in segment_files:
    if os.path.exists(fname):
        size_mb = os.path.getsize(fname) / (1024 * 1024)
        total_size += size_mb
        print(f"  ✓ {fname:<30} {size_mb:>8.2f} MB")

print("\n🔊 File Âm thanh:")
if os.path.exists("extracted_audio.wav"):
    size_kb = os.path.getsize("extracted_audio.wav") / 1024
    total_size += size_kb / 1024
    print(f"  ✓ extracted_audio.wav        {size_kb:>8.2f} KB")

if os.path.exists("extracted_audio.mp3"):
    size_kb = os.path.getsize("extracted_audio.mp3") / 1024
    total_size += size_kb / 1024
    print(f"  ✓ extracted_audio.mp3        {size_kb:>8.2f} KB")

for i in range(1, total_segments + 1):
    audio_file = f"segment_{i:02d}_audio.wav"
    if os.path.exists(audio_file):
        size_kb = os.path.getsize(audio_file) / 1024
        total_size += size_kb / 1024
        print(f"  ✓ {audio_file:<30} {size_kb:>8.2f} KB")

print("-" * 80)
print(f"  📊 Tổng dung lượng: {total_size:.2f} MB")

# Lưu thông tin vào JSON
info_json = "video_cutting_info.json"
video_info = {
    "filename": video_file,
    "width": width,
    "height": height,
    "fps": fps,
    "total_frames": total_frames,
    "duration": duration,
    "file_size_mb": os.path.getsize(video_file) / (1024 * 1024),
}

with open(info_json, "w") as f:
    json.dump(
        {
            "video": video_info,
            "segments": {
                "total": total_segments,
                "duration_per_segment": segment_duration,
                "files": segment_files,
            },
        },
        f,
        indent=2,
    )

print(f"\n💾 Thông tin lưu vào: {info_json}")

print("\n📋 THỐNG KÊ:")
print("-" * 80)
print(f"  • Video gốc: {video_file}")
print(f"  • Độ phân giải: {width} × {height}")
print(f"  • FPS: {fps}")
print(f"  • Thời lượng: {duration:.2f} giây")
print(f"  • Số đoạn cắt: {total_segments}")
print(f"  • Độ dài mỗi đoạn: {segment_duration} giây")
print(f"  • Tổng file: {len(output_files)}")
print(f"  • Tổng dung lượng: {total_size:.2f} MB")

print("\n" + "=" * 80)
print("✅ BÀI TẬP 12 HOÀN THÀNH")
print("=" * 80)
