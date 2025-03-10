def main():
    
    print("Factorial results using an iterative function")
    for num in [0, 5, 10, 25, 50, 100]:
        print(f"{num}! = {factorial_iterative(num)}")

    print("\nFactorial results using a recursive function")
    for num in [0, 5, 10, 25, 50, 100]:
        print(f"{num}! = {factorial_recursive(num)}")

    input("Press any key to continue...")


def factorial_iterative(n):
    """Calculates the factorial of a number iteratively using a for loop."""
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i
    return factorial

def factorial_recursive(n):
    """Calculates the factorial of a number recursively."""
    if n == 0:
        return 1
    else:
        return n * factorial_recursive(n - 1)

if __name__ == "__main__":
    main()

    