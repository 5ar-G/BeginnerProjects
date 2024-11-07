temp=float(input("Type in your temperature: "))
unit=input("Is that in Celsius or in Kelvin (C/K): ") .upper()

if unit== "K":
    temp= temp - 273.15
    print(f"That is {round(temp, 2)} °C")
elif unit== "C":
    temp = temp + 274.15
    print(f"That is {round(temp, 2)} K")
else:
    print("Please insert valid unit!")