menu = {
    # Hot Espresso Drinks
    1: {"category": "Hot Espresso Drinks", "name": "Latte", "price": 4.50, "flavorable": True, "milkable": True, "in_stock": True},
    2: {"category": "Hot Espresso Drinks", "name": "Cappuccino", "price": 4.25, "flavorable": True, "milkable": True, "in_stock": True},
    3: {"category": "Hot Espresso Drinks", "name": "Americano", "price": 3.50, "flavorable": False, "milkable": False, "in_stock": True},
    4: {"category": "Hot Espresso Drinks", "name": "Mocha", "price": 5.00, "flavorable": True, "milkable": True, "in_stock": True},

    # Cold Drinks
    5: {"category": "Cold Drinks", "name": "Iced Latte", "price": 4.50, "flavorable": True, "milkable": True, "in_stock": True},
    6: {"category": "Cold Drinks", "name": "Cold Brew", "price": 3.25, "flavorable": False, "milkable": False, "in_stock": True},
    7: {"category": "Cold Drinks", "name": "Iced Caramel Macchiato", "price": 5.25, "flavorable": True, "milkable": True, "in_stock": False},
    8: {"category": "Cold Drinks", "name": "Iced Mocha", "price": 5.25, "flavorable": True, "milkable": True, "in_stock": True},

    # Teas
    9: {"category": "Tea", "name": "Hot Green Tea", "price": 3.50, "flavorable": False, "milkable": False, "in_stock": True},
    10: {"category": "Tea", "name": "Iced Black Tea", "price": 3.25, "flavorable": False, "milkable": False, "in_stock": False},
    11: {"category": "Tea", "name": "Chai Latte", "price": 4.25, "flavorable": True, "milkable": True, "in_stock": False},

    # Decaf & Caffeine Free
    12: {"category": "Decaf & Caffeine-Free", "name": "Decaf Latte", "price": 4.50, "flavorable": True, "milkable": True, "in_stock": True},
    13: {"category": "Decaf & Caffeine-Free", "name": "Decaf Americano", "price": 3.50, "flavorable": False, "milkable": False, "in_stock": True},
    14: {"category": "Decaf & Caffeine-Free", "name": "Chamomile Tea", "price": 3.25, "flavorable": False, "milkable": False, "in_stock": True},
    15: {"category": "Decaf & Caffeine-Free", "name": "Hot Chocolate", "price": 4.00, "flavorable": True, "milkable": True, "in_stock": True},
}

# Upsize Options Available
sizes = {
    1: {"name": "Small", "extra": 0.00},
    2: {"name": "Medium", "extra": 0.75},
    3: {"name": "Large", "extra": 1.00},
}

# Additional Flavors
flavors = {
    1: {"name": "No Flavor", "extra": 0.00},
    2: {"name": "French Vanilla", "extra": 0.25},
    3: {"name": "Peppermint Mocha", "extra": 0.25},
    4: {"name": "Pumpkin Spice", "extra": 0.25},
    5: {"name": "Gingerbread", "extra": 0.25},
}

# Milk Options
milks = {
    1: {"name": "Whole Milk", "extra": 0.00},
    2: {"name": "Oat Milk", "extra": 0.25},
    3: {"name": "Almond Milk", "extra": 0.25},
}

# Toppings
toppings = {
    1: {"name": "No Toppings", "extra": 0.00},
    2: {"name": "Whipped Cream", "extra": 0.25},
    3: {"name": "Caramel Drizzle", "extra": 0.25},
    4: {"name": "Chocolate Drizzle", "extra": 0.25},
}

def get_valid_choice(options, prompt):
    while True:
        raw = input(prompt).strip()
        if raw.isdigit() and int(raw) in options:
            return int(raw)
        print("Invalid selection, please try again.")

def show_menu():
    last_category = ""
    for number, item in menu.items():
        if item["category"] != last_category:
            print(f"\n--- {item['category']} ---")
            last_category = item["category"]

        status = "" if item["in_stock"] else " (OUT OF STOCK)"
        print(f"{number}. {item['name']} - ${item['price']:.2f}{status}")

    print("\nPrices shown are for Small. Medium +$0.75. Large +$1.00.")
    print("Flavors +$0.25. Oat/Almond milk +$0.25. Toppings +$0.25.")


def place_order():
    show_menu()
    drink_number = get_valid_choice(menu, "\nEnter item number: ")

    if not menu[drink_number]["in_stock"]:
        print("Sorry, this item is currently unavailable.")
        return

    print(f"You chose: {menu[drink_number]['name']}")

    print("\nSizes:")
    for number, size in sizes.items():
        print(f"{number}. {size['name']} (+${size['extra']:.2f})")
    size_number = get_valid_choice(sizes, "Choose a size: ")

    if menu[drink_number]["milkable"]:
        print("\nMilk Options:")
        for number, milk in milks.items():
            print(f"{number}. {milk['name']} (+${milk['extra']:.2f})")
        milk_number = get_valid_choice(milks, "Choose a milk: ")
        milk_name = milks[milk_number]["name"]
        milk_extra = milks[milk_number]["extra"]
    else:
        milk_name = "None"
        milk_extra = 0.00

    if menu[drink_number]["flavorable"]:
        print("\nFlavors:")
        for number, flavor in flavors.items():
            print(f"{number}. {flavor['name']} (+${flavor['extra']:.2f})")
        flavor_number = get_valid_choice(flavors, "Choose a flavor: ")
        flavor_name = flavors[flavor_number]["name"]
        flavor_extra = flavors[flavor_number]["extra"]
    else:
        flavor_name = "None"
        flavor_extra = 0.00

    if menu[drink_number]["milkable"]:
        print("\nToppings:")
        for number, topping in toppings.items():
            print(f"{number}. {topping['name']} (+${topping['extra']:.2f})")
        topping_number = get_valid_choice(toppings, "Choose a topping: ")
        topping_name = toppings[topping_number]["name"]
        topping_extra = toppings[topping_number]["extra"]
    else:
        topping_name = "None"
        topping_extra = 0.00

    final_price = (menu[drink_number]["price"]
                   + sizes[size_number]["extra"]
                   + milk_extra
                   + flavor_extra
                   + topping_extra)
    print(f"\n{menu[drink_number]['name']} ({sizes[size_number]['name']}, {milk_name}, {flavor_name}, {topping_name}): ${final_price:.2f}")

def staff_sign_in():
    print("Staff sign-in coming soon.")

def main():
    while True:
        print ("\n===Ctrl+Alt+Decaf===")
        print("1. Place Order")
        print("2. Staff Sign-in")
        print("3. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            place_order()
        elif choice == "2":
            staff_sign_in()
        elif choice == "3":
            print("Thank you, have a great day!")
            break
        else:
            print("Invalid selection. Please try again.")

main()

