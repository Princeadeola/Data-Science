"""
 Variable Scope
In Python, we can declare variables in three different scopes: local scope, global, and nonlocal scope.

A variable scope specifies the region where we can access a variable. For example,

def add_numbers():
    sum = 5 + 4
Here, the sum variable is created inside the function, so it can only be accessed within it (local scope).
This type of variable is called a local variable.

Based on the scope, we can classify Python variables into three types:

Local Variables
Global Variables
Nonlocal Variables

"""


"""
Local Variables
When we declare variables inside a function, these variables will have a local scope (within the function). 
We cannot access them outside the function.
"""
print("..........Local Variable............")


def greet(name):
    message = "Hello"
    print(message, name)


greet("John")
# print(message) # error because message is local to greet function


"""
Global Variables
In Python, a variable declared outside of the function or in global scope is known as a global variable. 
This means that a global variable can be accessed inside or outside of the function
"""
print("\n")
print("..........Global Variable............")

message = "Good morning"


def greet(username):
    print(message, username)
    print("Local", message)


greet("Joe")
print("Global", message)

"""
Nonlocal Variables
In Python, nonlocal variables are used in nested functions whose local scope is not defined. 
This means that the variable can be neither in the local nor the global scope.

We use the nonlocal keyword to create nonlocal variables.
"""

