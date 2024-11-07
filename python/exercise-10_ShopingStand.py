menu = {"pizza": 2.46,
        "cookies": 1.73,
        "pancake": 4.6,
        "waffle": 5,
        "popcorns": 4.56,
        "nachos": 3,
        "fries": 2.50,
        "water": 2,
        "coke": 3.6,
        "sprite": 3}
cart = []
total = 0
print("----------MENU----------")
for key, value in menu.items():
    print(f"{key:10}: ${value:.2f}")
print("------------------------")

while True:
    food = input("Select item (Q to quit): ").lower()
    if food == "q":
        break
    elif menu.get(food) is not None:
        cart.append(food)

print("----------ORDER----------")
print()
for food in cart:
    total += menu.get(food)
    print(f"{food:10}: ${menu.get(food):.2f}")
print()
print(f"Your total is: ${total}")
print("------------------------")