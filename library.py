def validate_input(a, b):
    # Check if both inputs are numbers (int or float)
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        # If not, return False
        return False
    # If both inputs are numbers, return True
    return True

def add(a, b):
    # Validate inputs
    if not validate_input(a, b):
        # If not numbers, return error message
        return "Both inputs should be numbers"
    # If inputs are numbers, return sum
    return a + b

def subtract(a, b):
    # Validate inputs
    if not validate_input(a, b):
        # If not numbers, return error message
        return "Both inputs should be numbers"
    # If inputs are numbers, return difference
    return a - b

def multiply(a, b):
    # Validate inputs
    if not validate_input(a, b):
        # If not numbers, return error message
        return "Both inputs should be numbers"
    # If inputs are numbers, return product
    return a * b

def divide(a, b):
    # Validate inputs
    if not validate_input(a, b):
        # If not numbers, return error message
        return "Both inputs should be numbers"
    # Check if division by zero
    if b == 0:
        # If division by zero, return error message
        return "Cannot divide by zero"
    # If inputs are numbers and no division by zero, return quotient
    return a / b

def square_root(a):
    # Check if input is a number (int or float)
    if not isinstance(a, (int, float)):
        # If not a number, return error message
        return "Input should be a number"
    # Check if input is negative
    if a < 0:
        # If negative, return error message
        return "Cannot find square root of a negative number"
    # If input is positive, return square root
    return a ** 0.5

def exponentiation(a, b):
    # Validate inputs
    if not validate_input(a, b):
        # If not numbers, return error message
        return "Both inputs should be numbers"
    # If inputs are numbers, return result of exponentiation
    return a ** b

def interact():
    # Dictionary of operations
    operations = {
        1: add,
        2: subtract,
        3: multiply,
        4: divide,
        5: square_root,
        6: exponentiation
    }
    # Print menu of operations
    print("Select an operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Square root")
    print("6. Exponentiation")

    # Get user choice
    choice = int(input("Enter your choice (1-6): "))
    # Check if choice is valid
    if choice not in operations:
        # If not valid, return error message
        return "Invalid choice"

    # Get inputs based on choice of operation
    if choice in [1, 2, 3, 4]:
      #ask for number
        a = float(input("Enter first number: "))
      #ask for number
        b = float(input("Enter second number: "))
      #get result
        result = operations[choice](a, b)
    else:
      #get number
        a = float(input("Enter number: "))
      #result
        result = operations[choice](a)
      #print the result
    print("Result:", result)
#use the function
interact()
