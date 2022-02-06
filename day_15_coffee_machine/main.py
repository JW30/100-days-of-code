MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
profit = 0


def sufficient_resources(product):
    ingreds = MENU[product]["ingredients"]
    for item in ingreds:
        if resources[item] < ingreds[item]:
            print(f"Sorry, not enough {item} left.")
            return False
    return True


def process_and_evaluate_coins():
    cents = int(input("How many cents would you like to insert? "))
    euros = int(input("How many euros would you like to insert? "))
    money = euros + cents / 100
    cost = MENU[choice]["cost"]
    if money < cost:
        print("Sorry, that's not enough money. Money refunded")
        return False
    elif money > cost:
        print(f"Here is {round((money - cost), 2)}€ in change.")
    return True


def update_resources(product):
    ingreds = MENU[product]["ingredients"]
    for item in ingreds:
        resources[item] -= ingreds[item]


while True:
    choice = input("What would you like? (espresso/latte/cappuccino): ")
    if choice == "off":
        break
    elif choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Profit: {profit}€")
    else:
        if sufficient_resources(choice):
            if process_and_evaluate_coins():
                update_resources(choice)
                profit += MENU[choice]["cost"]
                print(f"Here is your {choice.capitalize()} ☕️. Enjoy!")
