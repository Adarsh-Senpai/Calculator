# Step 1: Define the calculator functions
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    return x / y

# Step 2: Display the menu
def display_menu():
    print("\n--- Simple Calculator ---")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")

# Step 3: Main program loop
def main():
    while True:
        display_menu()
        choice = input("\nSelect an operation (1-5): ")

        if choice == '5':
            print("\nExiting the calculator. Goodbye!")
            break

        # Validate user input for a valid operation
        if choice in ['1', '2', '3', '4']:
            try:
                num1 = float(input("\nEnter the first number: "))
                num2 = float(input("Enter the second number: "))

                if choice == '1':
                    print(f"\nResult: {num1} + {num2} = {add(num1, num2)}")
                elif choice == '2':
                    print(f"\nResult: {num1} - {num2} = {subtract(num1, num2)}")
                elif choice == '3':
                    print(f"\nResult: {num1} * {num2} = {multiply(num1, num2)}")
                elif choice == '4':
                    print(f"\nResult: {num1} / {num2} = {divide(num1, num2)}")
            except ValueError:
                print("\nInvalid input. Please enter numeric values.")
        else:
            print("\nInvalid choice. Please select a valid operation.")

# Run the calculator
main()
