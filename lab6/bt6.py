import os
import numpy as np
from pydub import AudioSegment
import soundfile as sf

print("=" * 70)
print("BÀI TẬP 6: GỘP HAI FILE ÂM THANH")
print("=" * 70)

# ============================================================================
# BƯỚC 1: CHUẨN BỊ CÁC FILE ÂM THANH
# ============================================================================

print("\n" + "=" * 70)
print("BƯỚC 1: CHUẨN BỊ CÁC FILE ÂM THANH")
print("=" * 70)

# Kiểm tra song1.wav
if not os.path.exists("song1.wav"):
    print("\n❌ File song1.wav không tìm thấy!")
    print("   Vui lòng chạy bt5.py trước để tạo file.")
    exit(1)

# Tạo song2.wav nếu chưa có
if not os.path.exists("song2.wav"):
    print("\n📝 Tạo file song2.wav (khác song1.wav)")

    sample_rate = 44100
    duration = 20  # 20 giây, ngắn hơn song1

    # Tạo dữ liệu âm thanh: tần số khác
    t = np.linspace(0, duration, int(sample_rate * duration))

    # Tạo giai điệu khác: tần số từ 220Hz đến 440Hz
    frequency = 220 + 220 * (t / duration)
    audio_data = np.sin(2 * np.pi * frequency * t)

    # Chuẩn hóa dữ liệu
    audio_data = (audio_data * 32767).astype(np.int16)

    # Lưu thành file WAV
    sf.write("song2.wav", audio_data, sample_rate)
    print(f"✓ Đã tạo file: song2.wav")
    print(f"  - Sample rate: {sample_rate} Hz")
    print(f"  - Duration: {duration} giây")
    print(f"  - File size: {os.path.getsize('song2.wav') / 1024:.2f} KB")

# Tải hai file âm thanh
print("\n📀 Đang tải hai file âm thanh...")
song1 = AudioSegment.from_file("song1.wav", format="wav")
song2 = AudioSegment.from_file("song2.wav", format="wav")

print(f"✓ Song1: {len(song1)/1000:.2f} giây")
print(f"✓ Song2: {len(song2)/1000:.2f} giây")

# ============================================================================
# BƯỚC 2: GỘP TRỰC TIẾP (song1 + song2)
# ============================================================================

print("\n" + "=" * 70)
print("BƯỚC 2: GỘP TRỰC TIẾP (song1 + song2)")
print("=" * 70)

merged_direct = song1 + song2
output_file_1 = "merged_direct.wav"
merged_direct.export(output_file_1, format="wav")

print(f"\n1️⃣  GỘP TRỰC TIẾP")
print(f"   ✓ File: {output_file_1}")
print(
    f"   ✓ Thời lượng: {len(song1)/1000:.2f}s + {len(song2)/1000:.2f}s = {len(merged_direct)/1000:.2f}s"
)
print(f"   ✓ Size: {os.path.getsize(output_file_1)/1024:.2f} KB")
print(f"   ✓ Cấu trúc: [Song1] → [Song2]")

# ============================================================================
# BƯỚC 3: GỘP VỚI KHOẢNG TRỐNG 2 GIÂY (song1 + silence + song2)
# ============================================================================

print("\n" + "=" * 70)
print("BƯỚC 3: GỘP VỚI KHOẢNG TRỐNG 2 GIÂY")
print("=" * 70)

# Tạo khoảng trống im lặng 2 giây
silence_duration = 2000  # 2000 ms = 2 giây
silence = AudioSegment.silent(duration=silence_duration)

merged_with_silence = song1 + silence + song2
output_file_2 = "merged_with_silence.wav"
merged_with_silence.export(output_file_2, format="wav")

print(f"\n2️⃣  GỘP VỚI KHOẢNG TRỐNG 2 GIÂY")
print(f"   ✓ File: {output_file_2}")
print(f"   ✓ Khoảng trống: {silence_duration/1000:.1f} giây")
print(
    f"   ✓ Thời lượng: {len(song1)/1000:.2f}s + {silence_duration/1000:.1f}s + {len(song2)/1000:.2f}s = {len(merged_with_silence)/1000:.2f}s"
)
print(f"   ✓ Size: {os.path.getsize(output_file_2)/1024:.2f} KB")
print(f"   ✓ Cấu trúc: [Song1] → [Silence 2s] → [Song2]")

# ============================================================================
# BƯỚC 4: GỘP VỚI CHỒNG LẶP 1 GIÂY
# ============================================================================

print("\n" + "=" * 70)
print("BƯỚC 4: GỘP VỚI CHỒNG LẶP 1 GIÂY")
print("=" * 70)

overlap_duration = 1000  # 1000 ms = 1 giây

# Lấy 1 giây cuối của song1
song1_overlap_part = song1[-overlap_duration:]

# Lấy 1 giây đầu của song2
song2_overlap_part = song2[:overlap_duration]

# Tính toán phần không chồng
song1_before_overlap = song1[:-overlap_duration]
song2_after_overlap = song2[overlap_duration:]

print(f"\n📊 Chi tiết chồng lặp:")
print(f"   • Song1 phần không chồng: {len(song1_before_overlap)/1000:.2f}s")
print(f"   • Phần chồng lặp: {overlap_duration/1000:.1f}s")
print(f"   • Song2 phần không chồng: {len(song2_after_overlap)/1000:.2f}s")

# Gộp phần chồng (trộn 2 âm thanh)
overlap_merged = song1_overlap_part.overlay(song2_overlap_part)

# Ghép lại: song1_before + overlap_merged + song2_after
merged_overlapped = song1_before_overlap + overlap_merged + song2_after_overlap
output_file_3 = "merged_overlapped.wav"
merged_overlapped.export(output_file_3, format="wav")

print(f"\n3️⃣  GỘP VỚI CHỒNG LẶP 1 GIÂY")
print(f"   ✓ File: {output_file_3}")
print(f"   ✓ Phương pháp: overlay (trộn âm thanh)")
print(f"   ✓ Thời lượng: {len(merged_overlapped)/1000:.2f}s")
print(f"   ✓ Size: {os.path.getsize(output_file_3)/1024:.2f} KB")
print(f"   ✓ Cấu trúc: [Song1 phần đầu] → [Chồng 1s] → [Song2 phần cuối]")

# ============================================================================
# BƯỚC 5: THỐNG KÊ VÀ SO SÁNH
# ============================================================================

print("\n" + "=" * 70)
print("BƯỚC 5: THỐNG KÊ VÀ SO SÁNH KẾT QUẢ")
print("=" * 70)

print("\n📊 SO SÁNH 3 PHƯƠNG PHÁP GỘP:")
print(f"\n{'Phương pháp':<30} {'Duration (s)':<15} {'File Size (KB)':<15} {'File'}")
print("-" * 70)

# Direct merge
print(
    f"{'Gộp trực tiếp':<30} {len(merged_direct)/1000:<15.2f} {os.path.getsize(output_file_1)/1024:<15.2f} {output_file_1}"
)

# With silence
print(
    f"{'Gộp + khoảng trống 2s':<30} {len(merged_with_silence)/1000:<15.2f} {os.path.getsize(output_file_2)/1024:<15.2f} {output_file_2}"
)

# Overlapped
print(
    f"{'Gộp + chồng lặp 1s':<30} {len(merged_overlapped)/1000:<15.2f} {os.path.getsize(output_file_3)/1024:<15.2f} {output_file_3}"
)

# Tính toán tiết kiệm
direct_size = os.path.getsize(output_file_1)
overlap_size = os.path.getsize(output_file_3)
saved_size = direct_size - overlap_size
saved_percent = (saved_size / direct_size) * 100

print(f"\n💾 So sánh kích thước:")
print(f"   • Gộp trực tiếp: {direct_size/1024:.2f} KB")
print(f"   • Gộp chồng lặp: {overlap_size/1024:.2f} KB")
print(f"   • Tiết kiệm: {saved_size/1024:.2f} KB ({saved_percent:.1f}%)")

# ============================================================================
# BƯỚC 6: THÔNG TIN CHI TIẾT
# ============================================================================

print("\n" + "=" * 70)
print("BƯỚC 6: THÔNG TIN CHI TIẾT VỀ CÁC FILE OUTPUT")
print("=" * 70)

output_files = [output_file_1, output_file_2, output_file_3]
descriptions = [
    "Gộp trực tiếp: song1 + song2",
    "Gộp có khoảng trống: song1 + 2s silence + song2",
    "Gộp chồng lặp: song1_part + overlay(1s) + song2_part",
]

for i, (file, desc) in enumerate(zip(output_files, descriptions), 1):
    if os.path.exists(file):
        audio = AudioSegment.from_file(file, format="wav")
        size_kb = os.path.getsize(file) / 1024
        duration = len(audio) / 1000

        print(f"\n{i}. {file}")
        print(f"   Mô tả: {desc}")
        print(f"   Size: {size_kb:.2f} KB")
        print(f"   Duration: {duration:.2f} giây")
        print(f"   Channels: {audio.channels}")
        print(f"   Sample rate: {audio.frame_rate} Hz")
        print(f"   Bit depth: 16-bit")

# ============================================================================
# BƯỚC 7: ĐỌC DỮ LIỆU CHI TIẾT BẰNG SOUNDFILE
# ============================================================================

print("\n" + "=" * 70)
print("BƯỚC 7: PHÂN TÍCH DỮ LIỆU CHI TIẾT BẰNG SOUNDFILE")
print("=" * 70)

# Đọc file merged_overlapped
data, sr = sf.read(output_file_3)
print(f"\n📖 Phân tích {output_file_3}:")
print(f"   ✓ Sample rate: {sr} Hz")
print(f"   ✓ Số samples: {len(data)}")
print(f"   ✓ Thời lượng: {len(data)/sr:.2f} giây")
print(f"   ✓ Min value: {np.min(data):.2f}")
print(f"   ✓ Max value: {np.max(data):.2f}")
print(f"   ✓ RMS (volume): {np.sqrt(np.mean(data**2)):.2f}")
