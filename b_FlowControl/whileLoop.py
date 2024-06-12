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


"""
while loop with break statement
We can use a break statement inside a while loop to terminate the 
loop immediately without checking the test condition. 
"""
print("\n")
print("..........while loop with break............")
while True:
    user_input = input("Enter your name: ")
    if user_input == "end":
        print("The loop ends here")
        break

    print(f"Hi {user_input}")

"""
while loop with an else clause
In Python, a while loop can have an optional else clause - that is executed once the loop condition is False
"""
print("\n")
print("..........while loop with else............")

number = 0;
while number < 3:
    print(f"current number is {number}")
    number = number + 1
else:
    print("Else block executed")
