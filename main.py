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

