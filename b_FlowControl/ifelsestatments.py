"""
if Statement
An if-statement executes a block of code only if the specified condition is met.

Syntax

if condition:
    # body of if statement
Here, if the condition of the if statement is:

True - the body of the if statement executes.
False - the body of the if statement is skipped from execution.
"""

print("..........If Statement............")
number = 5
if number > 0:
    print("number if positive")
print("This one will always execute regardless")


"""
if...else Statement
An if statement can have an optional else clause. The else statement executes if the condition in the if statement evaluates to False.

Syntax

if condition:
    # body of if statement

else:
    # body of else statement
Here, if the condition inside the if statement evaluates to

True - the body of if executes, and the body of else is skipped.
False - the body of else executes, and the body of if is skipped
"""

print("\n")
print(".......... If Else Statement............")
age = 17
if age > 16:
    print("You can do you man")
else:
    print("Go sleep young man")
print("This will always execute regardless of age")

"""
if…elif…else Statement
The if...else statement is used to execute a block of code among two alternatives.

However, if we need to make a choice between more than two alternatives, we use the if...elif...else statement.
"""

print("\n")
print("..........Else If Statement............")
age = 18
if age < 16:
    print("Have some rest")
elif age == 16:
    print("Go get work to do")
else:
    print("Start going man")

"""
Nested if Statements
It is possible to include an if statement inside another if statement. 
"""
print("\n")
print("..........Nested If Statement............")
country = "Nigeria"
age  = 16
location = "United Kingdom"
if country == "Nigeria":
    if age > 18:
        if location == "Nigeria":
            print("User is currently under the NG Laws")
        else:
            print("Exiting the location condition")
    else:
        print("Exiting the age condition")
else:
    print("Exiting the country condition")
print("Nested if completed")
