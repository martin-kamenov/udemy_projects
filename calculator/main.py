from art import logo

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def division(n1, n2):
    return n1 / n2 if n2 != 0 else 0

operations = {
    "+": add,
    "_": subtract,
    "*": multiply,
    "/": division
}

def calculator():
    print(logo)

    first_number = float(input("What's the first number?: "))
    continue_with_result = True

    while continue_with_result:
        [print(o) for o in operations.keys()]
        operator = input("Pick an operation: ")
        second_number = float(input("What's the next number?: "))
        result = operations[operator](first_number, second_number)
        print(f"{first_number} {operator} {second_number} = {result}")

        choice = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: \n")

        if choice == 'y':
            first_number = result
        else:
            continue_with_result = False
            print("\n" * 30)
            calculator()

calculator()
