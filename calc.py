def simple_calculator():
    """
    A simple calculator that takes two numbers and an operation as input.
    """
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        operation = input("Enter the operation (+, -, *, /): ")

        if operation == '+':
            result = num1 + num2
        elif operation == '-':
            result = num1 - num2
        elif operation == '*':
            result = num1 * num2
        elif operation == '/':
            if num2 == 0:
                print("Error: Division by zero is not allowed.")
                return
            result = num1 / num2
        else:
            print("Error: Invalid operation.")
            return

        print(f"Result: {result}")

    except ValueError:
        print("Error: Invalid number input. Please enter valid numbers.")

if __name__ == "__main__":
    simple_calculator()