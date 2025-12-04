import numpy as np

# Câu 1: Tạo các array và in properties

# 1. Tạo array từ list [1, 2, 3, 4, 5]
arr_from_list = np.array([1, 2, 3, 4, 5])
print("1. Array từ list:")
print(f"   Mảng: {arr_from_list}")
print(f"   Shape: {arr_from_list.shape}")
print(f"   Dtype: {arr_from_list.dtype}")
print(f"   Size: {arr_from_list.size}")
print(f"   Ndim: {arr_from_list.ndim}")
print()

# 2. Tạo array zeros: hình dạng (3, 4)
arr_zeros = np.zeros((3, 4))
print("2. Array zeros (3, 4):")
print(f"   Mảng:\n{arr_zeros}")
print(f"   Shape: {arr_zeros.shape}")
print(f"   Dtype: {arr_zeros.dtype}")
print(f"   Size: {arr_zeros.size}")
print(f"   Ndim: {arr_zeros.ndim}")
print()

# 3. Tạo array ones: hình dạng (2, 5)
arr_ones = np.ones((2, 5))
print("3. Array ones (2, 5):")
print(f"   Mảng:\n{arr_ones}")
print(f"   Shape: {arr_ones.shape}")
print(f"   Dtype: {arr_ones.dtype}")
print(f"   Size: {arr_ones.size}")
print(f"   Ndim: {arr_ones.ndim}")
print()

# 4. Tạo array ngẫu nhiên: hình dạng (3, 3)
arr_random = np.random.rand(3, 3)
print("4. Array ngẫu nhiên (3, 3):")
print(f"   Mảng:\n{arr_random}")
print(f"   Shape: {arr_random.shape}")
print(f"   Dtype: {arr_random.dtype}")
print(f"   Size: {arr_random.size}")
print(f"   Ndim: {arr_random.ndim}")
