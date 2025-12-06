import os
import wave
import struct
import numpy as np
from pydub import AudioSegment
from pydub.generators import Sine
import soundfile as sf

print("=" * 70)
print("BÀI TẬP 5: TẢI, PHÁT VÀ CHỈNH SỬA FILE ÂM THANH")
print("=" * 70)

# ============================================================================
# BƯỚC 1: TẠO FILE ÂM THANH TEST
# ============================================================================

print("\n" + "=" * 70)
print("BƯỚC 1: CHUẨN BỊ FILE ÂM THANH")
print("=" * 70)

# Tạo file MP3 test nếu chưa có
sample_rate = 44100  # 44.1 kHz
duration = 30  # 30 giây
audio_file = "song1.mp3"
wav_file = "song1.wav"

if not os.path.exists(audio_file) and not os.path.exists(wav_file):
    print(f"\n📝 Tạo file âm thanh test: {wav_file}")

    # Tạo dữ liệu âm thanh: tần số biến đổi (sóng hình sin)
    t = np.linspace(0, duration, int(sample_rate * duration))

    # Tạo giai điệu: tần số tăng từ 440Hz đến 880Hz
    frequency = 440 + 440 * (t / duration)
    audio_data = np.sin(2 * np.pi * frequency * t)

    # Chuẩn hóa dữ liệu
    audio_data = (audio_data * 32767).astype(np.int16)

    # Lưu thành file WAV
    sf.write(wav_file, audio_data, sample_rate)
    print(f"✓ Đã tạo file: {wav_file}")
    print(f"  - Sample rate: {sample_rate} Hz")
    print(f"  - Duration: {duration} giây")
    print(f"  - File size: {os.path.getsize(wav_file) / 1024:.2f} KB")

    # Chuyển đổi WAV sang MP3
    try:
        audio = AudioSegment.from_wav(wav_file)
        audio.export(audio_file, format="mp3")
        print(f"\n✓ Đã tạo file: {audio_file}")
        print(f"  - File size: {os.path.getsize(audio_file) / 1024:.2f} KB")
    except Exception as e:
        print(f"⚠ Không thể tạo MP3 (ffmpeg cần cài đặt): {e}")
        print(f"   Sử dụng WAV thay thế")
        audio_file = wav_file
else:
    if os.path.exists(audio_file):
        print(f"✓ Tìm thấy file: {audio_file}")
    elif os.path.exists(wav_file):
        print(f"✓ Tìm thấy file: {wav_file}")
        audio_file = wav_file

# ============================================================================
# BƯỚC 2: LOAD VÀ LẤY THÔNG TIN FILE ÂM THANH
# ============================================================================

print("\n" + "=" * 70)
print("BƯỚC 2: TẢI VÀ LẤY THÔNG TIN FILE ÂM THANH")
print("=" * 70)

try:
    # Sử dụng PyDub để load file
    if audio_file.endswith(".mp3"):
        print(f"\n📀 Đang tải file MP3: {audio_file}")
        audio = AudioSegment.from_mp3(audio_file)
    else:
        print(f"\n📀 Đang tải file WAV: {audio_file}")
        audio = AudioSegment.from_wav(audio_file)

    # Lấy thông tin
    print("\n✓ Thông tin file âm thanh:")
    print(f"  • Độ dài: {len(audio)} ms ({len(audio)/1000:.2f} giây)")
    print(f"  • Sample rate: {audio.frame_rate} Hz")
    print(f"  • Số kênh: {audio.channels}")
    print(f"  • Độ sâu bit: {audio.sample_width * 8} bit")
    print(f"  • Frame count: {len(audio.get_array_of_samples()) // audio.channels}")

    duration_seconds = len(audio) / 1000

except Exception as e:
    print(f"❌ Lỗi tải file: {e}")
    exit(1)

# ============================================================================
# BƯỚC 3: TRÍCH XUẤT VÀ XỬ LÝ ÂM THANH
# ============================================================================

print("\n" + "=" * 70)
print("BƯỚC 3: TRÍCH XUẤT VÀ XỬ LÝ ÂM THANH")
print("=" * 70)

# 1. Trích xuất 5 giây đầu tiên
print("\n1️⃣  Trích xuất 5 giây đầu tiên:")
first_5_sec = audio[:5000]  # 5000ms = 5 giây
output_file_1 = "audio_first_5sec.wav"
first_5_sec.export(output_file_1, format="wav")
print(f"   ✓ Lưu vào: {output_file_1}")
print(f"     - Độ dài: {len(first_5_sec)/1000:.2f} giây")

# 2. Lấy 10 giây giữa file (từ giây 15 đến 25)
print("\n2️⃣  Lấy 10 giây giữa (từ giây 15 đến giây 25):")
start_ms = 15 * 1000  # 15 giây
end_ms = 25 * 1000  # 25 giây

if duration_seconds >= 25:
    middle_segment = audio[start_ms:end_ms]
    output_file_2 = "audio_middle_10sec.wav"
    middle_segment.export(output_file_2, format="wav")
    print(f"   ✓ Lưu vào: {output_file_2}")
    print(f"     - Độ dài: {len(middle_segment)/1000:.2f} giây")
else:
    print(f"   ⚠ File quá ngắn ({duration_seconds:.1f}s), không thể lấy từ giây 15-25")
    print(
        f"     Thay vào đó: lấy từ giây {max(0, duration_seconds-10):.1f} đến {duration_seconds:.1f}"
    )
    middle_segment = audio[max(0, len(audio) - 10000) :]
    output_file_2 = "audio_middle_10sec.wav"
    middle_segment.export(output_file_2, format="wav")
    print(f"   ✓ Lưu vào: {output_file_2}")
    print(f"     - Độ dài: {len(middle_segment)/1000:.2f} giây")

# 3. Thay đổi âm lượng
print("\n3️⃣  Thay đổi âm lượng:")

# Tăng 6 dB
increase_db = 6
audio_louder = audio + increase_db
output_file_3a = "audio_louder_plus6db.wav"
audio_louder.export(output_file_3a, format="wav")
print(f"   ✓ Tăng âm lượng {increase_db} dB")
print(f"     - Lưu vào: {output_file_3a}")

# Giảm 6 dB
decrease_db = -6
audio_quieter = audio + decrease_db
output_file_3b = "audio_quieter_minus6db.wav"
audio_quieter.export(output_file_3b, format="wav")
print(f"   ✓ Giảm âm lượng {-decrease_db} dB")
print(f"     - Lưu vào: {output_file_3b}")

# 4. Lặp lại file 3 lần
print("\n4️⃣  Lặp lại file âm thanh 3 lần (concatenate):")
audio_repeated = audio + audio + audio
output_file_4 = "audio_repeated_3times.wav"
audio_repeated.export(output_file_4, format="wav")
print(f"   ✓ Lặp lại 3 bản (concatenate)")
print(f"     - Độ dài gốc: {len(audio)/1000:.2f} giây")
print(f"     - Độ dài mới: {len(audio_repeated)/1000:.2f} giây")
print(f"     - Lưu vào: {output_file_4}")

# ============================================================================
# BƯỚC 4: ĐỌC DỮ LIỆU ÂM THANH VỚI WAVE HOẶC SOUNDFILE
# ============================================================================

print("\n" + "=" * 70)
print("BƯỚC 4: ĐỌC DỮ LIỆU ÂM THANH VỚI SOUNDFILE")
print("=" * 70)

# Sử dụng soundfile để đọc file WAV
print(f"\n📖 Đọc file: {output_file_1}")
data, sr = sf.read(output_file_1)
print(f"   ✓ Sample rate: {sr} Hz")
print(f"   ✓ Số sample: {len(data)}")
print(f"   ✓ Shape: {data.shape}")
if len(data.shape) > 1:
    print(f"   ✓ Số kênh: {data.shape[1]}")
else:
    print(f"   ✓ Số kênh: 1 (Mono)")
print(f"   ✓ Độ sâu bit: 16-bit (standard)")

# ============================================================================
# BƯỚC 5: THỐNG KÊ CÁC FILE OUTPUT
# ============================================================================

print("\n" + "=" * 70)
print("BƯỚC 5: THỐNG KÊ CÁC FILE OUTPUT")
print("=" * 70)

output_files = [
    output_file_1,
    output_file_2,
    output_file_3a,
    output_file_3b,
    output_file_4,
]

print("\n📊 Các file âm thanh được tạo:")
total_size = 0
for i, file in enumerate(output_files, 1):
    if os.path.exists(file):
        size_kb = os.path.getsize(file) / 1024
        total_size += size_kb

        # Tải thông tin file
        try:
            audio_info = AudioSegment.from_wav(file)
            duration = len(audio_info) / 1000
            print(f"\n{i}. {file}")
            print(f"   - Size: {size_kb:.2f} KB")
            print(f"   - Duration: {duration:.2f} giây")
            print(f"   - Sample rate: {audio_info.frame_rate} Hz")
        except:
            print(f"\n{i}. {file} (Size: {size_kb:.2f} KB)")

print(f"\n💾 Tổng dung lượng: {total_size:.2f} KB")
