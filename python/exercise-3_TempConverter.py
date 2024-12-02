
#Function to check if a string is a number.
def is_float(value):
    try:
        float(value)  
        return True   
    except ValueError:
        return False
    

#Input.
temp = input("Enter the temperature: ")


#Checking if the input is a number.
if is_float(temp):
    temp = float(temp)
else:
    print("Invalid temperature. PLEASE TRY AGAIN!")
    exit()


#Input
unit = input("Is this in °C or K: ").upper()


#Checking if the input is valid and performing the operation.
if unit =="C":
    temp += 273.15
    print(f"That is {temp:.2f}K")
elif unit == "K":
    temp -= 273.15
    print(f"That is {temp:.2f}°C")
else:
    print("Invalid unit. PLEASE TRY AGAIN!")