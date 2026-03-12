# calculator_with_history.py

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error! Division by zero."
    return a / b

def save_history(entry):
    with open("history.txt", "a") as file:
        file.write(entry + "\n")

def show_history():
    try:
        with open("history.txt", "r") as file:
            print("\n----- Calculation History -----")
            print(file.read())
    except FileNotFoundError:
        print("No history found yet.")

def clear_history():
    open("history.txt", "w").close()
    print("History cleared successfully!")

while True:
    print("\n===== Simple Calculator =====")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Show History")
    print("6. Clear History")
    print("7. Exit")

    choice = input("Enter your choice (1-7): ")

    if choice in ['1', '2', '3', '4']:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            result = add(num1, num2)
            operation = f"{num1} + {num2} = {result}"

        elif choice == '2':
            result = subtract(num1, num2)
            operation = f"{num1} - {num2} = {result}"

        elif choice == '3':
            result = multiply(num1, num2)
            operation = f"{num1} * {num2} = {result}"

        elif choice == '4':
            result = divide(num1, num2)
            operation = f"{num1} / {num2} = {result}"

        print("Result:", result)
        save_history(operation)

    elif choice == '5':
        show_history()

    elif choice == '6':
        clear_history()

    elif choice == '7':
        print("Exiting calculator. Goodbye!")
        break

    else:
        print("Invalid choice. Please try again.")