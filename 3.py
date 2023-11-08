# Simple Calculator

# creating the math functions
def add(first_number, second_number):
    result = first_number + second_number
    print(f"Result: {result}")

def subtract(first_number, second_number):
    result = first_number - second_number
    print(f"Result: {result}")

def multiply(first_number, second_number):
    result = first_number * second_number
    print(f"Result: {result}")

def divide(first_number, second_number):
    result = first_number / second_number
    print(f"Result: {result}")

# calculator introduction
print("Welcome to simple calculator.")
print("I will add/subtract/multiple/divide any two numbers you provide.")
first_input = input("Enter in first number: ")
second_input = input("Enter in second number: ")
operation = input("Would you like to add/subtract/multiple/divide: ")

# explicitly convert string type to float type
first_number = float(first_input)
second_number = float(second_input)

if operation == "add":
    add(first_number, second_number)
elif operation == "subtract":
    subtract(first_number, second_number)
elif operation == "multiply":
    multiply(first_number, second_number)
elif operation == "divide":
    divide(first_number, second_number)
else:
    print("Sorry, I do not understand your request.")
