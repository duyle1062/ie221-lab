import random


def choose_level():
    print("\n=== CHOOSE DIFFICULTY LEVEL ===")
    print("1. Easy (1–10)")
    print("2. Medium (1–50)")
    print("3. Hard (1–100)")

    while True:
        choice = input("Enter the choice (1-3): ")
        if choice == "1":
            return 1, 10
        elif choice == "2":
            return 1, 50
        elif choice == "3":
            return 1, 100
        else:
            print("Invalid choice")


def play_game(low, high):
    secret = random.randint(low, high)
    attempts = 0

    print(f"\n The number is between {low} and {high}")

    while True:
        try:
            guess = int(input("Guess: "))
        except ValueError:
            print("Please enter an integer")
            continue

        if guess < low or guess > high:
            print(f"Please enter an integer between {low} and {high}")
            continue

        attempts += 1

        if guess < secret:
            print("Too low")
        elif guess > secret:
            print("Too high")
        else:
            print(f"Bingo!")
            print(f"Total attempts: {attempts}")
            return attempts


def show_statistics(total_games, wins, best_score):
    print("\n=== GAME STATISTICS ===")
    print(f"Total games played: {total_games}")
    print(f"Games won: {wins}")
    if total_games > 0:
        print(f"Win rate: {wins / total_games * 100:.1f}%")
    if best_score is not None:
        print(f"Best record: {best_score} attempts")


def advanced_guessing_game():
    total_games = 0
    wins = 0
    best_score = None

    print("Welcome to the ADVANCED NUMBER GUESSING GAME!")

    while True:
        print("\n=== MAIN MENU ===")
        print("1. Play game")
        print("2. Show statistics")
        print("0. Exit")

        choice = input("Enter the choice: ")

        if choice == "1":
            low, high = choose_level()
            total_games += 1
            attempts = play_game(low, high)
            wins += 1

            if best_score is None or attempts < best_score:
                best_score = attempts
                print("New high score!")
        elif choice == "2":
            show_statistics(total_games, wins, best_score)
        elif choice == "0":
            print("Exiting the program")
            break
        else:
            print("Invalid choice")


# --- Run program ---
advanced_guessing_game()
