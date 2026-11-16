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

# Pick-up Time Slots
pickup_times = {
    1: "ASAP (about 10 minutes)",
    2: "In 15 minutes",
    3: "In 30 minutes",
    4: "In 45 minutes",
    5: "In 1 hour",
}

# Confirmed orders are stored here
orders = []

# Staff accounts, entered by PIN (demo PINS for the prototype)
employees = {
    "6889": {"id": 1001, "name": "Nicholas", "role": "barista"},
    "2143": {"id": 1002, "name": "Ryatt", "role": "barista"},
    "9187": {"id": 1003, "name": "Ryley", "role": "barista"},
}

def get_valid_choice(options, prompt):
    while True:
        raw = input(prompt).strip()
        if raw.isdigit() and int(raw) in options:
            return int(raw)
        print("Invalid selection, please try again.")

def get_yes_no(prompt):
    while True:
        answer = input(prompt).strip().lower()
        if answer in ("y", "n"):
            return answer == "y"
        print("Please enter y or n.")

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

    print ("\nPick-up Times:")
    for number, slot in pickup_times.items():
        print(f"{number}. {slot}")
    pickup_number = get_valid_choice(pickup_times, "Choose a pickup time: ")
    pickup_time = pickup_times[pickup_number]

    final_price = (menu[drink_number]["price"]
                   + sizes[size_number]["extra"]
                   + milk_extra
                   + flavor_extra
                   + topping_extra)

    print("\n--- Order Summary ---")
    print(f"Drink:       {menu[drink_number]['name']}")
    print(f"Size:        {sizes[size_number]['name']}")
    print(f"Milk:        {milk_name}")
    print(f"Flavor:      {flavor_name}")
    print(f"Topping:     {topping_name}")
    print(f"Pickup Time: {pickup_time}")
    print(f"Total:      ${final_price:.2f}")

    if get_yes_no("\nConfirm order? (y/n):  "):
        order = {
            "number": len(orders) + 1,
            "drink": menu[drink_number]["name"],
            "size": sizes[size_number]["name"],
            "milk": milk_name,
            "flavor": flavor_name,
            "topping": topping_name,
            "pickup": pickup_time,
            "total": final_price,
        }
        orders.append(order)
        print(f"\nOrder #{order['number']} placed! Pay in person at pick-up.")
    else:
        print("\nOrder cancelled.")


def staff_sign_in():
    pin = input("Enter your 4-digit PIN: ").strip()

    if pin in employees:
        employee = employees[pin]
        print(f"\nWelcome, {employee['name']}!")
        return employee

    print("Incorrect PIN. Please try again.")
    return None

def staff_menu(employee):
    while True:
        print(f"\n--- Staff Menu ({employee['name']}) ---")
        print("1. Take Order")
        print("2. Sign Out")

        choice = input("Choose an option: ")

        if choice == "1":
            place_order()
        elif choice == "2":
            print("Signed Out.")
            break
        else:
            print("Invalid Selection. Please try again.")

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
            employee = staff_sign_in()
            if employee:
                staff_menu(employee)
        elif choice == "3":
            print("Thank you, have a great day!")
            break
        else:
            print("Invalid selection. Please try again.")

main()

