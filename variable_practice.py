
def multiply(number1, number2):
    print("The product is:", number1 * number2)

def add(number1, number2):
    print("The sum is:", number1 + number2)

def subtract(number1, number2):
    print("The difference is:", number1 - number2)

def divide(number1, number2):
    if number1 == 0 or number2 == 0:
        print("Division by zero")
        False
    else:
        print("The quotient is:", number1/number2)

def main():
    number1 = int(input("Enter the first number: "))
    number2 = int(input("Enter the second number: "))
    multiply(number1, number2)
    add(number1, number2)
    subtract(number1, number2)
    divide(number1, number2)

main()