def is_perfect(num):
    if num < 2:
        return False
    total = 0
    for i in range(1, num):
        if num % i == 0:
            total += i
    return total == num


def find_perfect_numbers(limit):
    if limit < 2:
        print("limit >= 2 required.")
        return

    print(f"Perfect numbers from 1 to {limit}:")
    found = False
    for num in range(2, limit + 1):
        if is_perfect(num):
            print(f"{num} is a perfect number")
            found = True

    if not found:
        print("No perfect numbers found")


try:
    n = int(input("n = "))
    find_perfect_numbers(n)
except ValueError:
    print("Invalid input")
