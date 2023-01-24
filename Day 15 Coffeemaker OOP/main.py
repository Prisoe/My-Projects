from coffee import MENU, resources
print("Welcome to Coffee maker 2.0")


def check_resources(ingredients):
    """Checks for amount of ingredients left in the machine"""
    for item in ingredients:
        if ingredients[item] > resources[item]:
            print(f"Sorry not enough {item}")
            return False
        return True


def process_coins():
    """Returns the total calculated from coins inserted."""
    print("Please insert coins.")
    total = int(input("how many quarters?: ")) * 0.25
    total += int(input("how many dimes?: ")) * 0.1
    total += int(input("how many nickles?: ")) * 0.05
    total += int(input("how many pennies?: ")) * 0.01
    return total

def is_transaction_successful(money, cost):
    """Checks to see if money is sufficient"""
    if money >= cost:
        change = round((money - cost), 2)
        print(f"Here's your {change}")
        return True
    else:
        print("Insufficient Funds")
        return False

def is_sufficient(name, ingredients):
    """Checks to see if ingredients are sufficient"""
    name = MENU[selection]
    for item in ingredients:
        if ingredients[item] >= resources[item]:
            print("Insufficient ingredients")
            return False
        return True

def make_coffee(ingredients):
    """Makes coffee if Ingredients are enough"""
    for item in ingredients:
        resources[item] -= ingredients[item]
        print(f"Here's your {selection}, enjoy!!!")
        return True

coffeemaker = True

selection = input("Please select your choice of coffee (espresso, latte, cappuccino): ")

while coffeemaker:
    if selection == "off":
        print("Turning Off")
        coffeemaker = False

    elif selection == "report":
        print(f"There is {resources['water']}ml left")
        print(f"There is {resources['milk']}ml left")
        print(f"There is {resources['coffee']}g left")
        coffeemaker = False

    elif selection == "refill":
        for item in resources:
            resources[item] += 250

        print(f"There is {resources['water']}ml left")
        print(f"There is {resources['milk']}ml left")
        print(f"There is {resources['coffee']}g left")
        coffeemaker = False

    else:
        drink = MENU[selection]
        if is_sufficient(drink, drink["ingredients"]):
            payment = process_coins()
            if is_transaction_successful(payment, drink["cost"]):
                make_coffee(drink["ingredients"])





