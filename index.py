from art import logo


#Addition
def add(n1, n2):
    return n1 + n2


#subtraction
def subtract(n1, n2):
    return n1 - n2


#multiplication
def multiply(n1, n2):
    return n1 * n2


#divide
def divide(n1, n2):
    return n1 / n2


operation = {"+": add, "-": subtract, "*": multiply, "/": divide}


def calculator():
    print(logo)
    numb1 = float(input("What is the first number?:"))
    for symbol in operation:
        print(symbol)
    should_continue = True

    while should_continue:
        operation_symbol = input("Pick an operation:")
        numb2 = float(input("What is the next number?:"))
        calculation_function = operation[operation_symbol]
        answer = calculation_function(numb1, numb2)

        print(f"{numb1} {operation_symbol} {numb2} = {answer}")
        print(f"Final answer is {answer}")
        print("\n")
        if input(
                f"Type 'y' to continue calculating with {answer}, or type 'n' to exit:"
        ) == 'y':
            numb1 = answer
        else:
            should_continue = False
            calculator()


calculator()
