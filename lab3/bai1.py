def read_int(prompt):
    while True:
        try:
            n = int(input(prompt))
            return n
        except ValueError:
            print("Error: Vui lòng nhập một số nguyên hợp lệ.")


so = read_int("Nhập một số nguyên: ")
print(f"Số đã nhập: {so}")
