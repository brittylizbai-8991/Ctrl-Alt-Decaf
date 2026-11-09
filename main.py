menu = {
    # Hot Espresso Drinks
    1: {"category": "Hot Espresso Drinks", "name": "Latte", "price": 4.50, "flavorable": True, "in_stock": True},
    2: {"category": "Hot Espresso Drinks", "name": "Cappuccino", "price": 4.25, "flavorable": True, "in_stock": True},
    3: {"category": "Hot Espresso Drinks", "name": "Americano", "price": 3.50, "flavorable": False, "in_stock": True},
    4: {"category": "Hot Espresso Drinks", "name": "Mocha", "price": 5.00, "flavorable": True, "in_stock": True},

    # Cold Drinks
    5: {"category": "Cold Drinks", "name": "Iced Latte", "price": 4.50, "flavorable": True, "in_stock": True},
    6: {"category": "Cold Drinks", "name": "Cold Brew", "price": 3.25, "flavorable": False, "in_stock": True},
    7: {"category": "Cold Drinks", "name": "Iced Caramel Macchiato", "price": 5.25, "flavorable": True, "in_stock": False},
    8: {"category": "Cold Drinks", "name": "Iced Mocha", "price": 5.25, "flavorable": True, "in_stock": True},

    # Teas
    9: {"category": "Tea", "name": "Hot Green Tea", "price": 3.50, "flavorable": False, "in_stock": True},
    10: {"category": "Tea", "name": "Iced Black Tea", "price": 3.25, "flavorable": False, "in_stock": False},
    11: {"category": "Tea", "name": "Chai Latte", "price": 4.25, "flavorable": True, "in_stock": False},

    # Decaf & Caffeine Free
    12: {"category": "Decaf & Caffeine-Free", "name": "Decaf Latte", "price": 4.50, "flavorable": True, "in_stock": True},
    13: {"category": "Decaf & Caffeine-Free", "name": "Decaf Americano", "price": 3.50, "flavorable": False, "in_stock": True},
    14: {"category": "Decaf & Caffeine-Free", "name": "Chamomile Tea", "price": 3.25, "flavorable": False, "in_stock": True},
    15: {"category": "Decaf & Caffeine-Free", "name": "Hot Chocolate", "price": 4.00, "flavorable": True, "in_stock": True},

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

def place_order():
    print("Ordering coming soon.")

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

