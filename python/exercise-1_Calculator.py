
#Function to check if a string is a number.
def is_float(value):
    try:
        float(value)  
        return True   
    except ValueError:
        return False
#Input
num1 = input("Enter 1st number: ")
num2 = input("Enter 2nd number: ")

#Checking if the input is a number.
if is_float(num1) :
    num1 = float(num1)
else:
    print("Invalid numbers! PLEASE TRY AGAIN!")
    exit()

if  is_float(num2):
    num2 = float(num2)
else:
    print("Invalid numbers! PLEASE TRY AGAIN!")
    exit()

#Asking for operator.
operator = input("Enter an operator (+, -, *, /): ")

#Checking if the operator is valid and performing the operation.
if operator == "+":
    print(round(num1 + num2, 3))
elif operator == "-":
    print(round(num1 - num2, 3))
elif operator == "*":
    print(round(num1 * num2, 3))
elif operator == "/":
    print(round(num1 / num2, 3))
else:
    print(f"{operator} is not valid operator. PLEASE TRY AGAIN!")

