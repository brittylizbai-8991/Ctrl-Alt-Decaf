import time
from datetime import datetime

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
    1: {"name": "Done / No Toppings", "extra": 0.00},
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

# Daily deals: item number --> percent off of the base price
daily_deals = {}

# Staff accounts, entered by PIN (demo PINS for the prototype)
employees = {
    "6889": {"id": 1001, "name": "Nicholas", "role": "barista"},
    "2143": {"id": 1002, "name": "Ryatt", "role": "barista"},
    "9187": {"id": 1003, "name": "Ryley", "role": "barista"},
    "1217": {"id": 2001, "name": "Brittany", "role": "manager"},
}
# Tracks failed sign-in attempts and the lockout timer
sign_in_state = {"failed": 0, "locked_until": 0}


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

def get_price(prompt):
    while True:
        raw = input(prompt).strip()
        try:
            value = float(raw)
        except ValueError:
            print("Please enter a number like 4.50.")
            continue
        if value > 0:
            return round(value, 2)
        print("Price must be more than 0.")

def get_percent(prompt):
    while True:
        raw = input(prompt).strip()
        if raw.isdigit() and 1 <= int(raw) <= 90:
            return int(raw)
        print("Please enter a whole number from 1 to 90.")

def show_menu():
    last_category = ""
    for number, item in menu.items():
        if item["category"] != last_category:
            print(f"\n--- {item['category']} ---")
            last_category = item["category"]

        status = "" if item["in_stock"] else " (OUT OF STOCK)"
        deal = ""
        if number in daily_deals:
            deal = f" (DAILY DEAL: {daily_deals [number]}% off)"
        print(f"{number}. {item['name']} - ${item['price']:.2f}{status}{deal}")

    print("\nPrices shown are for Small. Medium +$0.75. Large +$1.00.")
    print("Flavors +$0.25. Oat/Almond milk +$0.25. Toppings +$0.25.")


def place_order(employee=None):
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
        print("\nToppings  (add as many as you like, choose 1 when finished):")
        for number, topping in toppings.items():
            print(f"{number}. {topping['name']} (+${topping['extra']:.2f})")

        chosen_toppings = []
        topping_extra = 0.00

        while True:
            topping_number = get_valid_choice(toppings, "Add a topping (1 to finish): ")
            if topping_number == 1:
                break
            name = toppings [topping_number]["name"]
            if name in chosen_toppings:
                print(f"{name}  is already added.")
            else:
                chosen_toppings.append(name)
                topping_extra += toppings[topping_number]["extra"]
                print(f"Added {name}.")
        if chosen_toppings:
            topping_name = ",  ".join(chosen_toppings)
        else:
            topping_name = "No Toppings"
    else:
        topping_name = "None"
        topping_extra = 0.00

    print ("\nPick-up Times:")
    for number, slot in pickup_times.items():
        print(f"{number}. {slot}")
    pickup_number = get_valid_choice(pickup_times, "Choose a pickup time: ")
    pickup_time = pickup_times[pickup_number]

    base_price = menu[drink_number]["price"]
    if drink_number in daily_deals:
        base_price = round(base_price * (100-daily_deals[drink_number]) / 100, 2)

    final_price = (base_price
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
        if employee:
            entered_by = employee["name"]
            employee_id = employee["id"]
        else:
            entered_by = "Mobile customer"
            employee_id = ("N/A")

        order = {
            "number": len(orders) + 1,
            "drink": menu[drink_number]["name"],
            "size": sizes[size_number]["name"],
            "milk": milk_name,
            "flavor": flavor_name,
            "topping": topping_name,
            "pickup": pickup_time,
            "total": final_price,
            "entered_by": entered_by,
            "employee_id": employee_id,
            "timestamp": datetime.now().strftime("%Y-%m-%d %I:%M %p"),
            "status": "Pending",
        }

        orders.append(order)
        print(f"\nOrder #{order['number']} placed! Pay in person at pick-up.")
        print(f"Recorded: {entered_by}, ID {employee_id}, {order['timestamp']}")
    else:
        print("\nOrder cancelled.")

def show_queue():
    print("\n--- Order Queue ---")
    found = False

    for order in orders:
        if order["status"] == "Pending":
            print(f"\n#{order['number']}  {order['drink']} ({order['size']})")
            print(f"    Milk: {order['milk']} | Flavor: {order['flavor']} | Topping: {order['topping']}")
            print(f"    Pickup: {order['pickup']}")
            found = True

    if not found:
        print("No pending orders.")

def mark_order_done():
    show_queue()

    pending = {}
    for order in orders:
        if order["status"] == "Pending":
            pending[order["number"]] = order

    if not pending:
        return

    number = get_valid_choice(pending, "\nEnter order number to mark done: ")
    pending[number] ["status"] = "Done"
    print(f"Order #{number} marked done.")

def toggle_stock():
    show_menu()
    item_number = get_valid_choice(menu, "\nEnter item number to change: ")
    item = menu[item_number]

    if item ["in_stock"]:
        item["in_stock"] = False
        print(f"{item['name']} is now OUT OF STOCK.")
    else:
        item["in_stock"] = True
        print(f"{item['name']} is BACK IN STOCK.")

def update_menu_items():
    while True:
        print("\n--- Update Menu Items & Daily Deals ---")
        print("1. Change an item's price")
        print("2. Set a daily deal")
        print("3. Clear all daily deals")
        print("4. Back")

        choice = input("Choose an option: ")

        if choice == "1":
            show_menu()
            item_number = get_valid_choice(menu, "\nEnter item number: ")
            old_price = menu[item_number]["price"]
            new_price = get_price("Enter new Small price: $")
            menu[item_number]["price"] = new_price
            print(f"{menu[item_number]['name']} changed from ${old_price:.2f} to ${new_price:.2f}.")
        elif choice == "2":
            show_menu()
            item_number = get_valid_choice(menu, "\nEnter item number for the deal: ")
            percent = get_percent("Percent off (1 to 90): ")
            daily_deals[item_number] = percent
            print(f"Daily deal set: {menu[item_number]['name']} is {percent}% off.")
        elif choice == "3":
            daily_deals.clear()
            print("All daily deals cleared.")
        elif choice == "4":
            break
        else:
            print("Invalid Selection. Please try again.")

def pick_order(allowed_statuses):
    chosen = {}
    for order in orders:
        if order["status"] in allowed_statuses:
            chosen[order["number"]] = order
            print(f"#{order['number']}  {order['drink']} ({order['size']})  "
                  f"${order['total']:.2f}  [{order['status']}]")

    if not chosen:
        print("No eligible orders.")
        return None

    number = get_valid_choice(chosen, "\nEnter order number: ")
    return chosen[number]

def manage_discounts_refunds(employee):
    if employee["role"] != "manager":
        print("Manager access only.")
        return

    while True:
        print("\n--- Discounts & Refunds ---")
        print("1. Apply a discount to an order")
        print("2. Refund an order")
        print("3. Back")

        choice = input("Choose an option: ")

        if choice == "1":
            order = pick_order(("Pending", "Done"))
            if order:
                if "discount_percent" in order:
                    print("That order already has a discount.")
                else:
                    percent = get_percent("Percent off (1 to 90): ")
                    order["total"] = round(order["total"] * (100 - percent) / 100, 2)
                    order["discount_percent"] = percent
                    order["discount_by"] = employee["name"]
                    print(f"Order #{order['number']} discounted {percent}%. New total: ${order['total']:.2f}")
        elif choice == "2":
            order = pick_order(("Pending", "Done"))
            if order:
                if get_yes_no(f"Refund ${order['total']:.2f} for order #{order['number']}? (y/n): "):
                    order["status"] = "Refunded"
                    order["refunded_by"] = employee["name"]
                    print(f"Order #{order['number']} refunded.")
                else:
                    print("Refund cancelled.")
        elif choice == "3":
            break
        else:
            print("Invalid Selection. Please try again.")

def review_orders():
    print("\n--- Orders by Employee ---")

    if not orders:
        print("No orders yet.")
        return

    by_employee = {}
    for order in orders:
        key = f"{order['entered_by']}  (ID {order['employee_id']})"
        if key not in by_employee:
            by_employee[key] = []
        by_employee[key].append(order)

    for key, employee_orders in by_employee.items():
        print(f"\n{key}: {len(employee_orders)} order(s)")
        for order in employee_orders:
            notes = ""
            if "discount_percent" in order:
                notes += f" | {order['discount_percent']}% discount by {order['discount_by']}"
            if order ["status"] == "Refunded":
                notes += f" | refunded by {order['refunded_by']}"
            print(f"  #{order['number']}  {order['timestamp']}  {order['drink']}"
                  f"({order['size']})  ${order['total']:.2f}  [{order['status']}]{notes}")

def manager_menu(employee):
    while True:
        print(f"\n--- Manager Tools ({employee['name']}) ---")
        print("1. Update Menu Items & Daily Deals")
        print("2. Discounts & Refunds")
        print("3. Review Orders by Employee")
        print("4. Back")

        choice = input("Choose an option: ")
        if choice == "1":
            update_menu_items()
        elif choice == "2":
            manage_discounts_refunds(employee)
        elif choice == "3":
            review_orders()
        elif choice == "4":
            break
        else:
            print("Invalid Selection. Please try again.")

def staff_sign_in():
    now = time.time()
    if now < sign_in_state["locked_until"]:
        seconds_left = int(sign_in_state["locked_until"] - now) + 1
        print(f"Too many attempts. Try again in {seconds_left} seconds.")
        return None

    pin = input("Enter your 4-digit PIN: ").strip()

    if pin in employees:
        sign_in_state["failed"] = 0
        employee = employees[pin]
        print(f"\nWelcome, {employee['name']}!")
        return employee

    sign_in_state["failed"] += 1
    if sign_in_state["failed"] >= 3:
        sign_in_state["locked_until"] = time.time() + 30
        sign_in_state["failed"] = 0
        print("Too many attempts. Try again in 30 seconds.")
    else:
        print("Incorrect PIN. Please try again.")
    return None

def staff_menu(employee):
    while True:
        print(f"\n--- Staff Menu ({employee['name']}) ---")
        print("1. Take Order")
        print("2. View Order Queue")
        print("3. Mark Order Done")
        print("4. Mark Item Out of Stock / Back in Stock")
        print("5. Sign Out")
        if employee["role"] == "manager":
            print("6. Manager Tools")

        choice = input("Choose an option: ")

        if choice == "1":
            place_order(employee)
        elif choice == "2":
            show_queue()
        elif choice == "3":
            mark_order_done()
        elif choice == "4":
            toggle_stock()
        elif choice == "5":
            print("Signed Out.")
            break
        elif choice == "6" and employee["role"] == "manager":
            manager_menu(employee)
        elif choice == "6":
            print("Manager access only.")
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

