def menu_phep_toan():
    while True:
        print("\n=== MENU PHÉP TOÁN CƠ BẢN ===")
        print("1. Cộng hai số")
        print("2. Trừ hai số")
        print("3. Nhân hai số")
        print("4. Chia hai số")
        print("0. Thoát")

        choice = input("Nhập lựa chọn: ")

        if choice == "0":
            print("Kết thúc!")
            break

        if choice in ["1", "2", "3", "4"]:
            try:
                a = float(input("Nhập số thứ nhất: "))
                b = float(input("Nhập số thứ hai: "))
            except ValueError:
                print("Số không hợp lệ")
                continue

            if choice == "1":
                print(f"Kết quả: {a} + {b} = {a + b}")
            elif choice == "2":
                print(f"Kết quả: {a} - {b} = {a - b}")
            elif choice == "3":
                print(f"Kết quả: {a} × {b} = {a * b}")
            elif choice == "4":
                if b == 0:
                    print("Không thể chia cho 0")
                else:
                    print(f"Kết quả: {a} ÷ {b} = {a / b}")
        else:
            print("Vui lòng nhập lại")


if __name__ == "__main__":
    menu_phep_toan()
