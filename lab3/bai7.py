def print_square(n, char):
    print("Square pattern:")
    for i in range(n):
        print(char * n)


def print_right_triangle(n, char):
    print("Right triangle pattern:")
    for i in range(1, n + 1):
        print(char * i)


def print_isosceles_triangle(n, char):
    print("Isosceles triangle pattern:")
    for i in range(1, n + 1):
        spaces = " " * (n - i)
        stars = char * (2 * i - 1)
        print(spaces + stars)


def print_pyramid(n, char):
    print("Pyramid pattern:")
    for i in range(1, n + 1):
        spaces = " " * (n - i)
        stars = char * (2 * i - 1)
        print(spaces + stars + spaces)


def show_menu():
    print("\n=== PATTERN PRINTING MENU ===")
    print("1. Square")
    print("2. Right triangle")
    print("3. Isosceles triangle")
    print("4. Pyramid")
    print("0. Exit")


def main():
    while True:
        show_menu()
        choice = input("Enter the choice: ")

        if choice == "0":
            print("Exit program.")
            break
        elif choice in ["1", "2", "3", "4"]:
            try:
                n = int(input("Enter number of rows: "))
                if n <= 0:
                    print("Number of rows > 0 required")
                    continue
                char = input("Enter a character to print: ")
            except ValueError:
                print("Invalid input")
                continue

            if choice == "1":
                print_square(n, char)
            elif choice == "2":
                print_right_triangle(n, char)
            elif choice == "3":
                print_isosceles_triangle(n, char)
            elif choice == "4":
                print_pyramid(n, char)
        else:
            print("Invalid choice")


main()
