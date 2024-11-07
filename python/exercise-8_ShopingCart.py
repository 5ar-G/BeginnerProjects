foods = []
prices = []
total = 0

while True:
    food = input(f"Enter a food to buy (Q to quit): ")
    if food.upper() == "Q":
        break
    else:
        price = float(input(f"Enter te price of a {food}: $"))
        foods.append(food)
        prices.append(price)

print("-----YOUR CART-----")

for food in foods:
    print(food)
print("-------------------")

for price in prices:
    total+=price

print(f"Your total is: ${total}")
print("-------------------")