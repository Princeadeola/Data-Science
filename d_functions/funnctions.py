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