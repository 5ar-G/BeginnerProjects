
#Input.
weight = input("Enter your weight: ")


#Function to check if a string is a number.
def is_number(value):
    try:
        float(value)  
        return True   
    except ValueError:
        return False
    

#Checking if the input is a number.
if is_number(weight):
    weight = float(weight)
else:
    print("Invalid weight. PLEASE TRY AGAIN!")
    exit()


#Input
unit = input("Is this 'kg' ot 'lb': ").lower()


#Checking if the input is valid and performing the operation.
if unit == "kg":
    weight = weight * 2.2046
    print(f"That is {weight:.2f}lb.")
elif unit == "lb":
    weight = weight / 2.2046
    print(f"That is {weight:.2f}kg")
else:
    print("Invalid unit. PLEASE TRY AGAIN!")



