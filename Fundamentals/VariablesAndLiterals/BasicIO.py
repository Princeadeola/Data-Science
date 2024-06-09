"""
Output formatting
Sometimes we would like to format our output to make it look attractive.
This can be done by using the str.format() method. For example,
"""
x = 5
y = 10

print('The value of x is {} and y is {}'.format(x,y))

"""
Python Input
While programming, we might want to take the input from the user. In Python, we can use the input() function.
"""
num = input("Enter a number: ")
print("You entered: " + num)
print("data type of entered input is ", type(num))

userInput = int(input("Enter your age: "))
print("So your age is ", userInput)
print("data type is", type(userInput))
