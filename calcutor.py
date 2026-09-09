def divide(a: float, b: float) -> float:
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
    return a / b


# --- Input & Helper Functions ---

def get_number(prompt: str) -> float:
    """Safely prompts the user for a valid number."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def show_menu() -> None:
    """Displays available operations."""
    print("\n--- Calculator ---")
    print("1. Add (+)")
    print("2. Subtract (-)")
    print("3. Multiply (*)")
    print("4. Divide (/)")
    print("5. Exit")

def calculate(choice: str, num1: float, num2: float) -> float:
    """Routes the operands to the matching function."""
    operations = {
        "1": add,
        "2": subtract,
        "3": multiply,
        "4": divide
    }
    action = operations.get(choice)
    return action(num1, num2)


# --- Main Application Loop ---

def main() -> None:
    while True:
        show_menu()
        choice = input("Select an option (1-5): ").strip()

        if choice == "5":
            print("Goodbye!")
            break

        if choice not in {"1", "2", "3", "4"}:
            print("Invalid selection. Please choose 1, 2, 3, 4, or 5.")
            continue

        num1 = get_number("Enter the first number: ")
        num2 = get_number("Enter the second number: ")

        try:
            result = calculate(choice, num1, num2)
            print(f"Result: {result}")
        except ZeroDivisionError as err:
            print(f"Error: {err}")


if __name__ == "__main__":
    main()
