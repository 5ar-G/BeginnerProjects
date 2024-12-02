foods = []
prices = []
total = 0
def is_number(value):
    try:
        float(value)  
        return True   
    except ValueError:
        return False

while True:
    food = input("Enter a food to buy(Q to quit): ")
    if food.upper() == "Q":
        break
    else:
        price = input(f"Enter the price of {food}: $")
        
        if is_number(price):
            price = float(price)
            foods.append(food)
            prices.append(price)
        else:
            print("Invalid price. PLEASE TRY AGAIN!")
            exit()

print("-----YOUR CART-----")

for food in foods:
    print(food)
print("-------------------")

for price in prices:
    total+=price

print(f"Your total is: ${total}")
print("-------------------")