MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
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

# Start of Personal Code #

nec_espresso = list(MENU["espresso"]["ingredients"].values())
nec_latte = list(MENU["latte"]["ingredients"].values())
nec_cappuccino = list(MENU["cappuccino"]["ingredients"].values())

on_state = True


def compare_ingredients(new_order, resources_dict):  # Here drink list represents one of nec_espresso, nec_latte, etc.
    for keys in MENU[new_order]["ingredients"]:
        needed_ingredient_quantity = MENU[new_order]["ingredients"][keys]
        if resources_dict[keys] < needed_ingredient_quantity:
            print(f"Sorry there is not enough {keys} ")
            return False
    return True


def subtract_resources(new_order, resources_dict):
    for keys in MENU[new_order]["ingredients"]:
        resources_dict[keys] = resources_dict[keys] - MENU[new_order]["ingredients"][keys]


def check_money(inputted_money, new_order):
    required_money = MENU[new_order]["cost"]
    if inputted_money < required_money:
        print("Sorry that's not enough money. Money refunded. ")
        return False
    elif inputted_money > required_money:
        change = inputted_money - required_money
        print(f"here is ${change} in change")
        return True
    else:
        return True


def check_order(new_order, resources_dict):  # collects money and uses check_money to verify correct amount.
    if compare_ingredients(new_order, resources_dict):
        print("Please insert coins \n")
        quarters = float(input("How many quarters would you like to use? \n"))
        dimes = float(input("How many dimes would you like ot use? \n"))
        nickles = float(input("How many nickles would you like to use? \n"))
        pennies = float(input("How many pennies would you like to use? \n"))

        total_money = quarters * 0.25 + dimes * 0.10 + nickles * 0.05 + pennies * 0.01

        return check_money(total_money, new_order)

    else:
        return False


def order():
    global on_state
    new_order = input("What would you like? (espresso/latte/cappuccino) ")
    if new_order == "report":
        print(f"Water: {resources['water']}ml \n")
        print(f"Milk: {resources['milk']}ml \n")
        print(f"Coffee: {resources['coffee']}ml \n")
    elif new_order == "off":
        on_state = False
    else:
        if check_order(new_order, resources):
            subtract_resources(new_order, resources)
            print(f"Here is your {new_order}. Enjoy! ")


while on_state:
    order()
