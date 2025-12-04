import numpy as np

# Câu 2: Tạo array 2D, 3D, reshape, transpose

print("=" * 60)
print("CÂU 2: Array 2D, 3D, Reshape, Transpose")
print("=" * 60)
print()

# 1. Tạo array 2D: 3 hàng, 4 cột
arr_2d = np.arange(12).reshape(3, 4)
print("1. Array 2D (3 hàng, 4 cột):")
print(f"   Mảng:\n{arr_2d}")
print(f"   Shape: {arr_2d.shape}")
print(f"   Ndim: {arr_2d.ndim}")
print(f"   Size: {arr_2d.size}")
print()

# 2. Tạo array 3D: shape (2, 3, 4)
arr_3d = np.arange(24).reshape(2, 3, 4)
print("2. Array 3D (shape 2, 3, 4):")
print(f"   Mảng:\n{arr_3d}")
print(f"   Shape: {arr_3d.shape}")
print(f"   Ndim: {arr_3d.ndim}")
print(f"   Size: {arr_3d.size}")
print()

# 3. Reshape array 1D (12 phần tử) thành (3, 4)
arr_1d = np.arange(1, 13)  # [1, 2, 3, ..., 12]
print("3. Reshape array 1D (12 phần tử) thành (3, 4):")
print(f"   Array 1D: {arr_1d}")
arr_reshaped_1 = arr_1d.reshape(3, 4)
print(f"   Sau reshape (3, 4):\n{arr_reshaped_1}")
print(f"   Shape: {arr_reshaped_1.shape}")
print(f"   Ndim: {arr_reshaped_1.ndim}")
print(f"   Size: {arr_reshaped_1.size}")
print()

# 4. Reshape array 1D thành (2, 3, 2)
print("4. Reshape array 1D thành (2, 3, 2):")
arr_1d_2 = np.arange(1, 13)  # [1, 2, 3, ..., 12]
arr_reshaped_2 = arr_1d_2.reshape(2, 3, 2)
print(f"   Array 1D: {arr_1d_2}")
print(f"   Sau reshape (2, 3, 2):\n{arr_reshaped_2}")
print(f"   Shape: {arr_reshaped_2.shape}")
print(f"   Ndim: {arr_reshaped_2.ndim}")
print(f"   Size: {arr_reshaped_2.size}")
print()

# 5. Tạo transpose của array 2D
print("5. Transpose của array 2D:")
print(f"   Array 2D gốc:\n{arr_2d}")
arr_2d_transpose = arr_2d.T
print(f"   Array 2D sau transpose:\n{arr_2d_transpose}")
print(f"   Shape gốc: {arr_2d.shape}")
print(f"   Shape sau transpose: {arr_2d_transpose.shape}")
print()

print("=" * 60)
