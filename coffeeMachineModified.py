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
    for item in resources:
        if menu[choice][item] > resources[item]:
            print(f"Not enough {item}! Cannot make {choice}.")
            return False
    return True

def suggest_alternatives(exclude_choice):
    alternatives = []
    for drink in menu:
        if drink == exclude_choice:
            continue
        available = True
        for item in resources:
            if menu[drink][item] > resources[item]:
                available = False
                break
        if available:
            alternatives.append(drink)
    if alternatives:
        print("But we can offer you:", " or ".join(alternatives))
    else:
        print("Sorry, no drinks are available at the moment.")

def make_drink(choice):
    for j in resources:
        resources[j] -= menu[choice][j]
    print(f"{choice.title()} served! Please pay Rs{menu[choice]['price']}.")

def coffee_machine():
    print("Welcome to the Coffee Machine")
    while True:
        print("Menu: cappuccino | mocha | latte | exit")
        choice = input("What would you like? ").lower()
        try:
            if choice == "exit":
                print("Thank you for using the machine.")
                break
            elif choice not in menu:
                raise ValueError("Invalid option. Please choose from the menu.")
        except ValueError as e:
            print(e)
        else:
            if is_available(choice):
                make_drink(choice)
            else:
                suggest_alternatives(exclude_choice=choice)
        finally:
            print("Remaining resources:", resources)
            print("-" * 40)

coffee_machine()
