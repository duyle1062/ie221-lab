def bubble_sort(arr):
    print("Bubble Sort visualization:")
    n = len(arr)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
        print(arr)
    print("Sorted:", arr)


def selection_sort(arr):
    print("Selection Sort visualization:")
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
        print(arr)
    print("Sorted:", arr)


def insertion_sort(arr):
    print("Insertion Sort visualization:")
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
        print(arr)
    print("Sorted:", arr)


def show_menu():
    print("\n=== SORTING ALGORITHM VISUALIZATION ===")
    print("1. Bubble Sort")
    print("2. Selection Sort")
    print("3. Insertion Sort")
    print("0. Exit")


def main():
    while True:
        show_menu()
        choice = input("Enter the choice: ")

        if choice == "0":
            print("Exit program.")
            break
        elif choice in ["1", "2", "3"]:
            try:
                raw_input = input("Enter numbers separated by spaces: ")
                arr = [int(x) for x in raw_input.split()]
            except ValueError:
                print("Invalid input")
                continue

            if choice == "1":
                bubble_sort(arr.copy())
            elif choice == "2":
                selection_sort(arr.copy())
            elif choice == "3":
                insertion_sort(arr.copy())
        else:
            print("Invalid choice")


main()
