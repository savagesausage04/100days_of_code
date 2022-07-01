from art import logo

def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


operations = {"+": add, "-": subtract, "*": multiply, "/": divide}


def calculator():
    print(logo)
    num1 = float(input("Pick a number: "))
    for operation in operations:
        print(operation)
    should_continue = True

    while should_continue:
        operation_symbol = input("Pick an operation: ")
        num2 = float(input("Pick another number: "))
        calculations = operations[operation_symbol]
        answer = calculations(num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")

        if input("Type 'y' to continue calculating or type 'n' to start over: ") == "y":
            num1 = answer
        elif input("Type 'y' to continue calculating or type 'n' to start over: ") == "n":
            should_continue = False
            calculator()


calculator()
