operator=input("Enter an operator (+, -, *, /): ")
num1=float(input("Enter first number: "))
num2=float(input("Enter second number: "))

if operator == "+":
    print(round(num1 + num2, 3))
elif operator == "-":
    print(round(num1 - num2, 3))
elif operator == "*":
    print(round(num1 * num2, 3))
elif operator == "/":
    print(round(num1 / num2, 3))
else:
    print(f"{operator} is not valid operator. PLEASE TRY AGAIN")
