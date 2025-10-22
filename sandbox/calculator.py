# Define the math operation functions
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print("You can't divide by zero.")
        return None


# Create the calculator loop
while True:

    operator = input("Choose an operator +, -, *, / (press 'q' to qui): ")
    a = int(input("Choose the first digit: "))
    b = int(input("Choose the second digit: "))

    if operator == "+":
        result = add(a, b)

    elif operator == "-":
        result = subtract(a, b)

    elif operator == "*":
        result = multiply(a, b)

    elif operator == "/":
        result = divide(a, b)

    # Print the result
    print(f"{a} {operator} {b} = {result}\n")
        
