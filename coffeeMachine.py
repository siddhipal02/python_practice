resources = {
    "water": 100,
    "milk": 100,
    "coffee": 50
}

menu = {
    "cappuccino": {"water": 10, "milk": 10, "coffee": 3, "price": 70},
    "mocha": {"water": 15, "milk": 7, "coffee": 7, "price": 80},
    "latte": {"water": 5, "milk": 15, "coffee": 10, "price": 30}
}

def is_available(choice):
    for i in resources:
        if(menu[choice][i]> resources[i]):
             print(f"Not enough {i}! Cannot make {choice}.")
             return False
    return True


def make_drink(choice):
    for j in resources:
        resources[j] = resources[j] - menu[choice][j]
    print(f"{choice} served! Please pay Rs{menu[choice]['price']}.")


def coffee_machine():
    print("Welcome to the Python Coffee Machine")
    while True:
        print("Menu: cappuccino | mocha | latte | exit")
        choice = input("What would you like? ")

        if choice == "exit":
            print("Thank you for using the machine.")
            break
        elif choice in menu:
            if is_available(choice):
                make_drink(choice)
        else:
            print("Invalid option. Please choose from the menu.")

coffee_machine()