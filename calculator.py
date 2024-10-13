def calculator():
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    operation = input("Choose the operation:\n1) Addition\n2) Subtraction\n3) Multiplication\n4) Division\n5) Modulus\n")

    if operation == '1':
        return num1 + num2
    elif operation == '2':
        return num1 - num2
    elif operation == '3':
        return num1 * num2
    elif operation == '4':
        if num2 != 0:
            return num1 / num2
        else:
            return "Error! Division by zero."
    elif operation == '5':
        return num1 % num2
    else:
        return "Invalid operation. Please choose a valid option (1-5)."

result = calculator()
print("Result: ",result)
