"""A command-line calculator for basic arithmetic operations."""


def get_number(prompt):
    """Keep asking until the user enters a valid number."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a number, for example 12 or 3.5.")


def calculate(first_number, second_number, operation):
    """Perform the selected arithmetic operation and return its result."""
    if operation == "+":
        return first_number + second_number
    if operation == "-":
        return first_number - second_number
    if operation == "*":
        return first_number * second_number
    if operation == "/":
        if second_number == 0:
            return None
        return first_number / second_number
    return "invalid"


def main():
    print("--- Simple Calculator ---")

    while True:
        first_number = get_number("Enter the first number: ")
        second_number = get_number("Enter the second number: ")

        print("\nChoose an operation: +  -  *  /")
        operation = input("Enter operation: ").strip()
        result = calculate(first_number, second_number, operation)

        if result == "invalid":
            print("Invalid operation. Please choose +, -, *, or /.")
        elif result is None:
            print("Error: A number cannot be divided by zero.")
        else:
            print(f"Result: {first_number} {operation} {second_number} = {result}")

        again = input("\nDo you want to calculate again? (yes/no): ").strip().lower()
        if again not in ("yes", "y"):
            print("Thank you for using the calculator!")
            break


if __name__ == "__main__":
    main()
