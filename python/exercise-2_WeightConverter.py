weight=float(input("Enter your weight: "))
unit=input("Kg or lbs? (K or L): ") .upper()


if unit== "K":
    weight = weight * 2.2046
    print(f"That is {round(weight, 2)} lbs")
elif unit== "L":
    weight = weight / 2.2046
    print(f"That is {round(weight, 2)} Kgs")
else:
    print("Invalid unit")
