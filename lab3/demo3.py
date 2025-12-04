import random


def game_doan_so():
    secret_number = random.randint(1, 100)
    attempt = 0

    while True:
        try:
            guess = int(input("Đoán số (1-100): "))
        except ValueError:
            print("Vui lòng nhập một số nguyên hợp lệ")
            continue

        attempt += 1

        if guess < 1 or guess > 100:
            print("Số nằm ngoài phạm vi. Hãy nhập lại")
            continue

        if guess < secret_number:
            print("Số thực tế lớn hơn")
        elif guess > secret_number:
            print("Số thực tế nhỏ hơn")
        else:
            print(f"Đúng! Số cần đoán là {secret_number}. Bạn đã đoán {attempt} lần.")
            break


game_doan_so()
