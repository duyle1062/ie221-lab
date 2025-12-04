def factorial_for(n):
    if n < 0:
        return None
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


def factorial_while(n):
    if n < 0:
        return None
    result = 1
    i = 1
    while i <= n:
        result *= i
        i += 1
    return result


while True:
    try:
        n = int(input("n = "))
        if n < 0:
            print("Error: n >= 0 required.")
        else:
            break
    except ValueError:
        print("Error: Please enter a valid integer.")

print(f"Factorial of n (using for loop): {factorial_for(n)}")
print(f"Factorial of n (using while loop): {factorial_while(n)}")
