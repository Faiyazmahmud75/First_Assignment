print("""Select operation:
1.Add
2.Subtract
3.Multiply
4.Divide
5.Modulus""")
math_operation = 0
#Loop to ensure a numerical value
while True:
    try:
        math_operation = int(input("Enter your choice (1/2/3/4/5)"))
        break
    except ValueError:
        print("Pleas enter a numerical value")
# Loop to ensure a option between 1 and 5
while math_operation > 5 or math_operation < 1:
    try:
        math_operation = int(input("Please enter a valid option between 1 and 5: "))
    except ValueError:
        print("Invalid input! Please enter a numerical value between 1 and 5")
# Loop to ensure the operand is a valid number
while True:
    try:
        num1 = float(input("Enter first number: "))
        break
    except ValueError:
        print("Invalid input for first number! Please enter valid numbers.")
# Same thing for the second number's variable
while True:
    try:
        num2 = float(input("Enter second number: "))
        break
    except ValueError:
        print("Invalid input for second number! Please enter valid numbers")
#functions for the mathematical operations
def addition(a,b):
    return a+b
def subtraction(a,b):
    return a-b
def multiplication(a,b):
    return a*b
def division(a,b):
    try:
        return a / b
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
def modulus(a,b):
    try:
        return a % b
    except ZeroDivisionError:
        print("Error: Try a number except 0")
# function execution code goes below
try:
    if math_operation == 1:
        result = addition(num1, num2)
        print(f"{num1} + {num2} =", result)
    elif math_operation == 2:
        result = subtraction(num1, num2)
        print(f"{num1} - {num2} =", result)
    elif math_operation == 3:
        result = multiplication(num1, num2)
        print(f"{num1} * {num2} =", result)
    elif math_operation == 4:
            result = division(num1, num2)
            print(f"{num1} / {num2} =", result)
    elif math_operation == 5:
        result = modulus(num1, num2)
        print(f"{num1} % {num2} =", result)
except Exception as e:
    print(e)

