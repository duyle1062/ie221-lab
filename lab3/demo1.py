def kiem_tra_nguyen_to(n):
    """Kiểm tra một số có phải là số nguyên tố không"""
    if n < 2:
        return False
    elif n == 2:
        return True
    else:
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True


# Test
n = int(input("Nhập số cần kiểm tra: "))

result = "là số nguyên tố" if kiem_tra_nguyen_to(n) else "không là số nguyên tố"
print(f"{n} {result}")
