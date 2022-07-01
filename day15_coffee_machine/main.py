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


def make_espresso():
    print("Please insert coins.")
    quarter_num = int(input("How many quarters?: "))
    dime_num = int(input("How many dimes?: "))
    nickel_num = int(input("How many nickels?: "))
    penny_num = int(input("How many pennies?: "))
    money_inputted = (0.25 * quarter_num) + (0.1 * dime_num) + (0.05 * nickel_num) + (0.01 * penny_num)
    if money_inputted < 1.5:
        print("Sorry that's not enough money. Money refunded.")
    elif money_inputted > 1.5:
        change = round((money_inputted - 1.5), 2)
        print(f"Here is ${change} in change.")
        print("Here is your espresso. Enjoy!")


def make_latte():
    print("Please insert coins.")
    quarter_num = int(input("How many quarters?: "))
    dime_num = int(input("How many dimes?: "))
    nickel_num = int(input("How many nickels?: "))
    penny_num = int(input("How many pennies?: "))
    money_inputted = (0.25 * quarter_num) + (0.1 * dime_num) + (0.05 * nickel_num) + (0.01 * penny_num)
    if money_inputted < 2.5:
        print("Sorry that's not enough money. Money refunded.")
    elif money_inputted > 2.5:
        change = round((money_inputted - 2.5), 2)
        print(f"Here is ${change} in change.")
        print("Here is your latte. Enjoy!")


def make_cappuccino():
    print("Please insert coins.")
    quarter_num = int(input("How many quarters?: "))
    dime_num = int(input("How many dimes?: "))
    nickel_num = int(input("How many nickels?: "))
    penny_num = int(input("How many pennies?: "))
    money_inputted = (0.25 * quarter_num) + (0.1 * dime_num) + (0.05 * nickel_num) + (0.01 * penny_num)
    if money_inputted < 3.0:
        print("Sorry that's not enough money. Money refunded.")
    elif money_inputted > 3.0:
        change = round((money_inputted - 3.0), 2)
        print(f"Here is ${change} in change.")
        print("Here is your cappuccino. Enjoy!")


def use_machine():
    still_running = True
    water_amount = 300
    milk_amount = 200
    coffee_amount = 100
    money_amount = 0

    while still_running:
        coffee_choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
        if coffee_choice == "espresso":
            water_deduction = 50
            coffee_deduction = 18
            if water_amount >= water_deduction and coffee_amount >= coffee_deduction:
                water_amount -= water_deduction
                coffee_amount -= coffee_deduction
                make_espresso()
            else:
                is_running = False
                print("Sorry, we are out of ingredients.")

        if coffee_choice == "latte":
            water_deduction = 200
            milk_deduction = 150
            coffee_deduction = 24
            if water_amount >= water_deduction and coffee_amount >= coffee_deduction and milk_amount >= milk_deduction:
                water_amount -= water_deduction
                coffee_amount -= coffee_deduction
                milk_amount -= milk_deduction
                make_latte()
            else:
                is_running = False
                print("Sorry, we are out of ingredients.")

        if coffee_choice == "cappuccino":
            water_deduction = 250
            milk_deduction = 100
            coffee_deduction = 24
            if water_amount >= water_deduction and coffee_amount >= coffee_deduction and milk_amount >= milk_deduction:
                water_amount -= water_deduction
                coffee_amount -= coffee_deduction
                milk_amount -= milk_deduction
                make_cappuccino()
            else:
                is_running = False
                print("Sorry, we are out of ingredients.")

        if coffee_choice == "report":
            print(f"{water_amount}ml water")
            print(f"{milk_amount}ml milk")
            print(f"{coffee_amount}g coffee")
            print(f"${money_amount}")

        if coffee_choice == "off":
            still_running = False


use_machine()
