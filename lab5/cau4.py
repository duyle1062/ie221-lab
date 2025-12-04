import numpy as np

# Câu 4: Tính MSE, RMSE, MAE

print("=" * 70)
print("CÂU 4: Mean Squared Error (MSE), Root MSE (RMSE), Mean Absolute Error (MAE)")
print("=" * 70)
print()

# 1. Tạo actual values (giá trị thực tế)
y_actual = np.array([3, -0.5, 2, 7])
print("1. Actual values (y):")
print(f"   {y_actual}")
print()

# 2. Tạo predicted values (giá trị dự đoán)
y_predicted = np.array([2.5, 0.0, 2, 8])
print("2. Predicted values (ŷ):")
print(f"   {y_predicted}")
print()

# 3. Tính sai số (residuals)
errors = y_actual - y_predicted
print("3. Sai số (y - ŷ):")
print(f"   {errors}")
print()

# 4a. Tính MSE (Mean Squared Error)
# MSE = (1/n) * Σ(y_i - ŷ_i)²
mse = np.mean(errors**2)
print("4a. MSE (Mean Squared Error):")
print(f"    Công thức: MSE = (1/n) * Σ(y_i - ŷ_i)²")
print(f"    Errors²: {errors ** 2}")
print(f"    MSE = {mse}")
print()

# 4b. Tính RMSE (Root Mean Squared Error)
# RMSE = √MSE = √[(1/n) * Σ(y_i - ŷ_i)²]
rmse = np.sqrt(mse)
print("4b. RMSE (Root Mean Squared Error):")
print(f"    Công thức: RMSE = √[(1/n) * Σ(y_i - ŷ_i)²]")
print(f"    RMSE = √{mse} = {rmse}")
print()

# 4c. Tính MAE (Mean Absolute Error)
# MAE = (1/n) * Σ|y_i - ŷ_i|
mae = np.mean(np.abs(errors))
print("4c. MAE (Mean Absolute Error):")
print(f"    Công thức: MAE = (1/n) * Σ|y_i - ŷ_i|")
print(f"    |Errors|: {np.abs(errors)}")
print(f"    MAE = {mae}")
print()

# Tóm tắt kết quả
print("=" * 70)
print("TÓM TẮT KẾT QUẢ:")
print("=" * 70)
print(f"MSE  = {mse:.6f}")
print(f"RMSE = {rmse:.6f}")
print(f"MAE  = {mae:.6f}")
print("=" * 70)
