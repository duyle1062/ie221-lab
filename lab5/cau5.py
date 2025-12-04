import pandas as pd
import numpy as np

# Cau 5 (2.2.1): Load va Kham pha du lieu tu salaries.csv

print("=" * 80)
print("CAU 5 (2.2.1): LOAD VA KHAM PHA DU LIEU - SALARIES.CSV")
print("=" * 80)
print()

# 1. Doc file salaries.csv
df = pd.read_csv("salaries.csv")
print("1. Doc file salaries.csv")
print("   * File da duoc doc thanh cong")
print()

# 2. In du lieu trong file
print("2. Du lieu trong file (10 dong dau tien):")
print(df.head(10))
print()

# 3. So luong mau du lieu va thuoc tinh
n_samples, n_features = df.shape
print("3. Kich thuoc bo du lieu:")
print(f"   So luong mau (dong): {n_samples}")
print(f"   So luong thuoc tinh (cot): {n_features}")
print()

# 4. Liet ke cac thuoc tinh
print("4. Danh sach cac thuoc tinh:")
print(f"   {list(df.columns)}")
print()

# 5. Xac dinh kieu du lieu
print("5. Kieu du lieu cua cac thuoc tinh:")
print(df.dtypes)
print()

# 6. Thong ke so luong gia tri cua moi thuoc tinh
print("6. So luong gia tri (info):")
df.info()
print()

# 7. Thong ke so luong gia tri rong (null)
print("7. So luong gia tri rong (null) cua moi thuoc tinh:")
null_counts = df.isnull().sum()
print(null_counts)
print()

# Kiem tra va loai bo dong chua gia tri rong
if null_counts.sum() > 0:
    print("   ! Phat hien gia tri rong! Loai bo cac dong chua null...")
    df_clean = df.dropna()
    print(f"   So dong truoc: {n_samples}, So dong sau: {len(df_clean)}")
    print(f"   Da xoa {n_samples - len(df_clean)} dong")
    df = df_clean
else:
    print("   * Khong co gia tri rong")
print()

# 8. Xac dinh cac nganh nghe lien quan den Data
print("8. Cac nganh nghe lien quan den Data (chua tu 'Data'):")
# Tim cot job title (co the la 'job_title', 'Job Title', vv)
job_col = None
for col in df.columns:
    if "job" in col.lower() and "title" in col.lower():
        job_col = col
        break

if job_col:
    data_jobs = df[df[job_col].str.contains("Data", case=False, na=False)]
    print(f"   Tong so nganh nghe co 'Data': {len(data_jobs)}")
    print(f"   Danh sach cac nganh nghe 'Data':")
    unique_data_jobs = data_jobs[job_col].unique()
    for job in unique_data_jobs:
        print(f"      - {job}")
else:
    print("   ! Khong tim thay cot job title")
print()

# 9. Sap xep bo du lieu theo muc luong giam dan va in 250 dong dau tien
print("9. Sap xep theo muc luong (USD) giam dan - Top 250 dong:")
# Tim cot salary (co the la 'salary_in_usd', 'Salary', 'salary USD', vv)
salary_col = None
for col in df.columns:
    if "salary" in col.lower():
        salary_col = col
        break

if salary_col:
    df_sorted = df.sort_values(by=salary_col, ascending=False)
    print(f"   Sap xep theo cot: '{salary_col}'")
    print(f"\n   Top 250 dong dau tien:")
    print(df_sorted.head(250).to_string())
else:
    print("   ! Khong tim thay cot salary")
print()

# 10. Thong ke so luong gia tri duy nhat cua moi thuoc tinh
print("10. So luong gia tri duy nhat (unique) cua moi thuoc tinh:")
unique_counts = df.nunique()
print(unique_counts)
print()

print("=" * 80)
print("* Phan tich du lieu hoan thanh")
print("=" * 80)
