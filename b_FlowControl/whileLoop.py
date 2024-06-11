"""
while Loop
In Python, we use the while loop to repeat a block of code until a certain condition is met.

while Loop Syntax
while condition:
    # body of while loop
Here,

The while loop evaluates the condition.
If the condition is true, body of while loop is executed. The condition is evaluated again.
This process continues until the condition is False.
Once the condition evaluates to False, the loop terminates.
"""

number = 1
while number <= 3:
    print(number)
    number = number + 1  # number += 1


# Calculate the sum of numbers until user enters 0
number = int (input("Enter number: "))

total = 0
while number != 0:
    total = total + number
    number = int (input("Enter number: "))

print("Total addition is ", total)
