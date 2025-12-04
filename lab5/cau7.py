import pandas as pd
import numpy as np

# Load data
df = pd.read_csv('salaries.csv')

# Remove rows with null values
df = df.dropna()

# Find salary column
salary_col = None
for col in df.columns:
    if 'salary' in col.lower():
        salary_col = col
        break

print("=" * 80)
print("CAU 7 (2.2.3): THONG KE DU LIEU")
print("=" * 80)

print(f"\nDu lieu sau khi loai bo null: {len(df)} hang\n")

# 1. Find median (mean) of salary for first 500 and all data
print("1. Trung vi (Mean) luong cua USD:")

mean_first_500 = df[salary_col].head(500).mean()
mean_all = df[salary_col].mean()

print(f"   - 500 nguoi dau tien: ${mean_first_500:,.2f}")
if mean_first_500 <= 50000:
    print("     -> Muc luong thap")
else:
    print("     -> Muc luong cao")

print(f"   - Toan bo du lieu: ${mean_all:,.2f}")
if mean_all <= 50000:
    print("     -> Muc luong thap")
else:
    print("     -> Muc luong cao")

# 2. Convert USD to VND (1 USD = 23575 VND)
print("\n2. Quy doi luong USD sang VND (1 USD = 23,575 VND):")

USD_TO_VND = 23575
df['salary_in_vnd'] = df[salary_col] * USD_TO_VND

print(f"   - Da them cot salary_in_vnd")
print(f"   - 5 hang dau tien:")
for idx, row in df.head(5).iterrows():
    print(f"      {idx+1}. {row[salary_col]:.0f} USD = {row['salary_in_vnd']:,.0f} VND")

# 3. Calculate total salary for first 500 and all data
print("\n3. Tong luong USD va VND:")

total_usd_500 = df[salary_col].head(500).sum()
total_vnd_500 = df['salary_in_vnd'].head(500).sum()

total_usd_all = df[salary_col].sum()
total_vnd_all = df['salary_in_vnd'].sum()

print(f"   - 500 nguoi dau tien:")
print(f"     USD: ${total_usd_500:,.0f}")
print(f"     VND: {total_vnd_500:,.0f}")

print(f"   - Toan bo du lieu ({len(df)} hang):")
print(f"     USD: ${total_usd_all:,.0f}")
print(f"     VND: {total_vnd_all:,.0f}")

# 4. Count and group by job title, save to CSV
print("\n4. Thong ke so luong nhan luc theo nganh nghe:")

# Find job title column
job_col = None
for col in df.columns:
    if 'job' in col.lower() or 'title' in col.lower():
        job_col = col
        break

job_counts = df[job_col].value_counts().reset_index()
job_counts.columns = ['job_title', 'number_of_people']
job_counts = job_counts.sort_values('number_of_people', ascending=False)

# Save to CSV
job_counts.to_csv('job_resource.csv', index=False)
print(f"   - Da luu vao file job_resource.csv")
print(f"   - Tong so nganh nghe: {len(job_counts)}")

# Find max and min
max_job = job_counts.iloc[0]
min_job = job_counts.iloc[-1]

print(f"\n   - Nganh nghe co so luong nhan luc CAO NHAT:")
print(f"     {max_job['job_title']}: {max_job['number_of_people']} nguoi")

print(f"\n   - Nganh nghe co so luong nhan luc THAP NHAT:")
print(f"     {min_job['job_title']}: {int(min_job['number_of_people'])} nguoi")

# Show top 10 jobs
print(f"\n   - Top 10 nganh nghe theo so luong nhan luc:")
for idx, row in job_counts.head(10).iterrows():
    print(f"     {idx+1}. {row['job_title']}: {row['number_of_people']} nguoi")

# 5. Save to Excel
print("\n5. Xuat file Excel:")

excel_file = 'salaries.xlsx'
df.to_excel(excel_file, index=False)
print(f"   - Da luu file Excel: {excel_file}")

print("\n" + "=" * 80)
print("* Thong ke du lieu hoan thanh")
print("=" * 80)
