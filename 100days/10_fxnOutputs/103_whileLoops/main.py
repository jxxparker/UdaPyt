#calculator
def add(n1, n2):
    return n1 + n2
def subtract(n1, n2):
    return n1 - n2
def multiply(n1, n2):
    return n1 * n2
def divide(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

def calculator():
    print("welcome to the calculator ;) ")
    num1 = int(input("what is the first number: ")) #asking first number
    for symbol in operations: #printing the number
        print(symbol) 
    should_continue = True

    while should_continue: #should continue is true
        operation_symbol = input("Pick an operation: ")
        num2 = int(input("what is the next number: "))
        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1, num2)

        print(f"{num1} {operation_symbol} {num2} = {answer}")

        if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ") == "y":
            num1 = answer
        else:
            should_continue = False
            calculator() #goes back up and runs the calculator fxn again. pretty much resetting
    
calculator()
