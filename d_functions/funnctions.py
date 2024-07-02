"""
A function is a block of code that performs a specific task.

Suppose we need to create a program to make a circle and color it. We can create two functions to solve this problem:

function to create a circle
function to color the shape

Dividing a complex problem into smaller chunks makes our program easy to understand and reuse.

"""

print("..........Functions without argument ............")


def greet():
    print("hello world")


greet()

print("\n")
print("..........Functions with args............")


def greet(name):
    print("You are welcome", name)


greet("Micheal")

print("\n")
print("..........Functions to add numbers............")


def addNumbers(a, b):
    print(a, "+", b, "=", (a + b))


addNumbers(2, 3)

print("\n")
print("..........Functions (Return statement)............")


# We return a value from the function using the return statement.


def squareNumber(num):
    result = num * num
    return result


answer = squareNumber(2)
print("result is", answer)

"""
Default Arguments in Functions
Python allows functions to have default argument values. Default arguments are used when no 
explicit values are passed to these parameters during a function call.

"""
print("\n")
print("..........Arguments in Functions............")


def greetings(name, greeting="Hello"):
    print(greeting, name)


greetings("John")

greetings("James", "Good morning")

"""
*args in Functions

Using *args allows a function to take any number of positional arguments.
"""

print("\n")
print("..........*args Arguments in Functions............")


def sumAllNumbers(*numbers):
    return sum(numbers)


print(sumAllNumbers(1, 2, 3, 4))

"""
*kwargs in Functions

Using **kwargs allows the function to accept any number of keyword arguments.
"""

print("\n")
print("..........*kwargs Arguments in Functions............")


def greet(**words):
    for key, value in words.items():
        print(f"{key} : {value}")


greet(name="John", greeting="Good morning", home="Lon", )
