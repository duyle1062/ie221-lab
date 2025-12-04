def classify(score):
    if score >= 8.5:
        return "Excellent"
    elif score >= 7.0:
        return "Good"
    elif score >= 5.0:
        return "Average"
    else:
        return "Poor"


def add_student(students):
    name = input("Enter student name: ").strip()
    try:
        score = float(input("Enter student score (0–10): "))
        if score < 0 or score > 10:
            print("Score between 0 and 10 required")
            return
        students[name] = score
        print(f"Added: {name} - {score}")
    except ValueError:
        print("Invalid score")


def show_students(students):
    if not students:
        print("Empty student list")
        return

    print("\n=== STUDENT LIST ===")
    for name, score in students.items():
        print(f"{name:20} | Score: {score:4.1f} | Grade: {classify(score)}")


def show_statistics(students):
    if not students:
        print("No data")
        return

    count = {"Excellent": 0, "Good": 0, "Average": 0, "Poor": 0}
    for score in students.values():
        grade = classify(score)
        count[grade] += 1

    print("\n=== STATISTICS ===")
    for grade, num in count.items():
        print(f"{grade:10}: {num} student(s)")


def show_min_max(students):
    if not students:
        print("No data")
        return

    max_score = max(students.values())
    min_score = min(students.values())

    print("\n=== HIGHEST SCORE ===")
    for name, score in students.items():
        if score == max_score:
            print(f"{name} - {score}")

    print("\n=== LOWEST SCORE ===")
    for name, score in students.items():
        if score == min_score:
            print(f"{name} - {score}")


def manage_scores():
    students = {}

    while True:
        print("\n=== STUDENT SCORE MANAGEMENT ===")
        print("1. Add new student")
        print("2. Show all students")
        print("3. Show grade statistics")
        print("4. Show highest and lowest scores")
        print("0. Exit")

        choice = input("Enter the choice: ")

        if choice == "1":
            add_student(students)
        elif choice == "2":
            show_students(students)
        elif choice == "3":
            show_statistics(students)
        elif choice == "4":
            show_min_max(students)
        elif choice == "0":
            print("Exiting the program")
            break
        else:
            print("Invalid choice")


# --- Run program ---
manage_scores()
