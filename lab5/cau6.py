import pandas as pd
import numpy as np

# Cau 6 (2.2.2): Loc du lieu va Phan tich Luong

print("=" * 80)
print("CAU 6 (2.2.2): LOC DU LIEU")
print("=" * 80)
print()

# Load du lieu
df = pd.read_csv("salaries.csv")

# Loai bo cac hang co gia tri null
df_clean = df.dropna()

print("Du lieu sau khi loai bo null: {} hang".format(len(df_clean)))
print()

# 1. Tim muc luong cao nhat, thap nhat, trung binh cua 500 nguoi dau tien
print("1. Thong ke luong cua 500 nguoi dau tien:")
first_500 = df_clean.head(500)
max_salary_500 = first_500["Salary"].max()
min_salary_500 = first_500["Salary"].min()
avg_salary_500 = first_500["Salary"].mean()
print(f"   - Luong cao nhat: ${max_salary_500:,.2f}")
print(f"   - Luong thap nhat: ${min_salary_500:,.2f}")
print(f"   - Luong trung binh: ${avg_salary_500:,.2f}")
print()

# 2. Tim muc luong cao nhat, thap nhat, trung binh cua ca bo du lieu
print("2. Thong ke luong cua ca bo du lieu ({} hang):".format(len(df_clean)))
max_salary_all = df_clean["Salary"].max()
min_salary_all = df_clean["Salary"].min()
avg_salary_all = df_clean["Salary"].mean()
print(f"   - Luong cao nhat: ${max_salary_all:,.2f}")
print(f"   - Luong thap nhat: ${min_salary_all:,.2f}")
print(f"   - Luong trung binh: ${avg_salary_all:,.2f}")
print()

# 3. Xac dinh cac nganh nghe co muc luong cao nhat
print("3. Cac nganh nghe co muc luong cao nhat (${:,.2f}):".format(max_salary_all))
max_salary_jobs = df_clean[df_clean["Salary"] == max_salary_all]
print(f"   - So nganh nghe: {len(max_salary_jobs)}")
for idx, row in max_salary_jobs.iterrows():
    print(
        f"      {row['Job Title']} - Age: {row['Age']}, Exp: {row['Years of Experience']} years"
    )
print()

# 4. Xac dinh cac nganh nghe co muc luong thap nhat
print("4. Cac nganh nghe co muc luong thap nhat (${:,.2f}):".format(min_salary_all))
min_salary_jobs = df_clean[df_clean["Salary"] == min_salary_all]
print(f"   - So nganh nghe: {len(min_salary_jobs)}")
for idx, row in min_salary_jobs.iterrows():
    print(
        f"      {row['Job Title']} - Age: {row['Age']}, Exp: {row['Years of Experience']} years"
    )
print()

# 5. Thong ke so luong nguoi co muc luong tren 50000 USD
print("5. Thong ke so luong nguoi co muc luong tren $50,000:")
high_salary_count = len(df_clean[df_clean["Salary"] > 50000])
high_salary_percent = (high_salary_count / len(df_clean)) * 100
print(f"   - So luong nguoi: {high_salary_count} / {len(df_clean)}")
print(f"   - Ty le: {high_salary_percent:.2f}%")
print()

# 6. Xac dinh cac nganh nghe co muc luong tren 50000 USD
print("6. Cac nganh nghe co muc luong tren $50,000:")
high_salary_df = df_clean[df_clean["Salary"] > 50000]
unique_jobs = high_salary_df["Job Title"].unique()
print(f"   - Tong so nganh nghe: {len(unique_jobs)}")
print(f"   - Danh sach cac nganh nghe:")
for i, job in enumerate(unique_jobs, 1):
    job_count = len(high_salary_df[high_salary_df["Job Title"] == job])
    avg_salary_job = high_salary_df[high_salary_df["Job Title"] == job]["Salary"].mean()
    print(f"      {i}. {job} - ({job_count} nguoi, Luong TB: ${avg_salary_job:,.2f})")
print()

# 7. Thong ke theo Education Level
print("7. Thong ke luong theo Education Level (trong nhan vien co luong > $50,000):")
education_stats = high_salary_df.groupby("Education Level")["Salary"].agg(
    ["count", "mean", "min", "max"]
)
print(education_stats.to_string())
print()

# 8. Thong ke theo Gender
print("8. Thong ke luong theo Gender (trong nhan vien co luong > $50,000):")
gender_stats = high_salary_df.groupby("Gender")["Salary"].agg(
    ["count", "mean", "min", "max"]
)
print(gender_stats.to_string())
print()

print("=" * 80)
print("* Phan tich du lieu hoan thanh")
print("=" * 80)
