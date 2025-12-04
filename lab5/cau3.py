import numpy as np

# Câu 3: Tính toán trên array (sum, mean, min, max, argmin, argmax)

print("=" * 70)
print("CÂU 3: Aggregation và Statistical Operations")
print("=" * 70)
print()

# 1. Tạo array 2D: (4, 5)
arr = np.array(
    [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20]]
)
print("1. Array 2D (4, 5):")
print(f"   {arr}")
print(f"   Shape: {arr.shape}, Dtype: {arr.dtype}")
print()

# 2. Tính tổng toàn bộ: sum()
total_sum = arr.sum()
print("2. Tổng toàn bộ array (sum()):")
print(f"   Tổng: {total_sum}")
print()

# 3. Tính tổng theo hàng (axis=1)
sum_axis1 = arr.sum(axis=1)
print("3. Tổng theo hàng (axis=1):")
print(f"   Kết quả: {sum_axis1}")
print()

# 4. Tính tổng theo cột (axis=0)
sum_axis0 = arr.sum(axis=0)
print("4. Tổng theo cột (axis=0):")
print(f"   Kết quả: {sum_axis0}")
print()

# 5a. Tính mean (toàn bộ)
mean_all = arr.mean()
print("5a. Mean toàn bộ array:")
print(f"   Mean: {mean_all}")
print()

# 5b. Tính mean theo hàng (axis=1)
mean_axis1 = arr.mean(axis=1)
print("5b. Mean theo hàng (axis=1):")
print(f"   Kết quả: {mean_axis1}")
print()

# 5c. Tính mean theo cột (axis=0)
mean_axis0 = arr.mean(axis=0)
print("5c. Mean theo cột (axis=0):")
print(f"   Kết quả: {mean_axis0}")
print()

# 6a. Tính min (toàn bộ)
min_all = arr.min()
print("6a. Min toàn bộ array:")
print(f"   Min: {min_all}")
print()

# 6b. Tính min theo hàng (axis=1)
min_axis1 = arr.min(axis=1)
print("6b. Min theo hàng (axis=1):")
print(f"   Kết quả: {min_axis1}")
print()

# 6c. Tính min theo cột (axis=0)
min_axis0 = arr.min(axis=0)
print("6c. Min theo cột (axis=0):")
print(f"   Kết quả: {min_axis0}")
print()

# 7a. Tính max (toàn bộ)
max_all = arr.max()
print("7a. Max toàn bộ array:")
print(f"   Max: {max_all}")
print()

# 7b. Tính max theo hàng (axis=1)
max_axis1 = arr.max(axis=1)
print("7b. Max theo hàng (axis=1):")
print(f"   Kết quả: {max_axis1}")
print()

# 7c. Tính max theo cột (axis=0)
max_axis0 = arr.max(axis=0)
print("7c. Max theo cột (axis=0):")
print(f"   Kết quả: {max_axis0}")
print()

# 8a. Tìm vị trí min: argmin() (toàn bộ, trong flattened array)
argmin_all = arr.argmin()
print("8a. Vị trí min (argmin) toàn bộ array:")
print(f"   Index trong flattened array: {argmin_all}")
print(f"   Giá trị tại vị trí đó: {arr.flatten()[argmin_all]}")
print()

# 8b. Tìm vị trí min theo hàng (axis=1)
argmin_axis1 = arr.argmin(axis=1)
print("8b. Vị trí min theo hàng (axis=1):")
print(f"   Kết quả: {argmin_axis1}")
print()

# 8c. Tìm vị trí min theo cột (axis=0)
argmin_axis0 = arr.argmin(axis=0)
print("8c. Vị trí min theo cột (axis=0):")
print(f"   Kết quả: {argmin_axis0}")
print()

# 9a. Tìm vị trí max: argmax() (toàn bộ, trong flattened array)
argmax_all = arr.argmax()
print("9a. Vị trí max (argmax) toàn bộ array:")
print(f"   Index trong flattened array: {argmax_all}")
print(f"   Giá trị tại vị trí đó: {arr.flatten()[argmax_all]}")
print()

# 9b. Tìm vị trí max theo hàng (axis=1)
argmax_axis1 = arr.argmax(axis=1)
print("9b. Vị trí max theo hàng (axis=1):")
print(f"   Kết quả: {argmax_axis1}")
print()

# 9c. Tìm vị trí max theo cột (axis=0)
argmax_axis0 = arr.argmax(axis=0)
print("9c. Vị trí max theo cột (axis=0):")
print(f"   Kết quả: {argmax_axis0}")
print()

print("=" * 70)
