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


# TODO 1.Print resource's report.
def print_report():
    """Print actual resource's report."""
    water, milk, coffee = resources['water'], resources['milk'], resources['coffee']

    print(f"Water: {water}ml\n"
          f"Milk: {milk}ml\n"
          f"Coffee: {coffee}g\n"
          f"Money: ${profit:.2f}")


# TODO 2.Check if resources are sufficient to make a drink.
def is_resources_sufficient(order_ingredients):
    """Returns True if resources are sufficient to purchase the drink, else returns False."""
    for resource in order_ingredients:
        if resources[resource] < order_ingredients[resource]:
            print("Sorry there is not enough water.")
            return False
    return True


# TODO 3.Process coins.
def insert_coins():
    """Returns total calculated coins inserted by user."""
    print("Please insert coins.")

    total = int(input("How many quarters?: ")) * 0.25
    total += int(input("How many dimes?: ")) * 0.10
    total += int(input("How many nickles?: ")) * 0.5
    total += int(input("How many pennies?: ")) * 0.1

    return total


# TODO 4.Check if transaction was successful.
def is_transaction_successful(received_money, drink_cost):
    """Returns True if purchase can be made and add the drink cost to the profit else returns False."""
    if received_money >= drink_cost:
        change = round(received_money - drink_cost, 2)
        print(f"Here is ${change} dollars in change.")
        global profit
        profit += drink_cost
        return True
    else:
        print(f"Sorry that's not enough money. Money refunded.")
        return False


# TODO 5.Make the coffee.
def make_coffee(drink_name, order_ingredients):
    """Deduct required ingredients from resources."""
    for ingredient in order_ingredients:
        resources[ingredient] -= order_ingredients[ingredient]

    print(f"Here is your {drink_name}. Enjoy!")

profit = 0

while True:
    action = input("What would you like? (espresso/latte/cappuccino): ")

    if action == "off":
        break
    elif action == "report":
        print_report()
    else:
        drink = MENU[action]

        if is_resources_sufficient(drink['ingredients']):
            if is_transaction_successful(insert_coins(), drink['cost']):
                make_coffee(action, drink['ingredients'])
