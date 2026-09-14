print("Hello Sir this is a calculator program. Please enter your operation: (+, -, *, /)")
operation = input()
if operation == "+":
    print("Enter two numbers:")
    num1 = float(input())
    num2 = float(input())
    result = num1 + num2
    print("The result is:", result)
elif operation == "-":
    print("Enter two numbers:")
    num1 = float(input())
    num2 = float(input())
    result = num1 - num2
    print("The result is:", result)
elif operation == "*":
    print("Enter two numbers:")
    num1 = float(input())
    num2 = float(input())
    result = num1 * num2
    print("The result is:", result)
elif operation == "/":
    print("Enter two numbers:")
    num1 = float(input())
    num2 = float(input())
    if num2 != 0:
        result = num1 / num2
        print("The result is:", result)
    else:
        print("Error: Division by zero is not allowed.")