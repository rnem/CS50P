"""
CS50 - Math Interpreter
Author: Roger Nem
About: Program that enables users to do math

x is an integer
y is +, -, *, or /
z is an integer

x, y, z = expression.split(" ")
will assign 1 to x, + to y, and 1 to z.
"""

expression = input("Expression: ")
x, y, z = expression.split(" ")

first_number = float(x)
operator = y
last_number = float(z)

match operator:
    case "+":
        result = first_number + last_number
    case "-":
        result = first_number - last_number
    case "*":
        result = first_number * last_number
    case "/":
        result = first_number / last_number

# Return the result of the operation
print(round(result,1))
