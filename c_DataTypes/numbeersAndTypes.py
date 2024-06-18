"""
Python Numbers, Type Conversion and Mathematics
The number data types are used to store the numeric values.

Python supports integers, floating-point numbers and complex numbers.
They are defined as int, float, and complex classes in Python.

int - holds signed integers of non-limited length.
float - holds floating decimal points and it's accurate up to 15 decimal places.
complex - holds complex numbers.
"""

"""
Numeric Data Type
Integers and floating points are separated by the presence or absence of a decimal point. For instance,

5 is an integer
5.42 is a floating-point number.
Complex numbers are written in the form, x + yj, where x is the real part and y is the imaginary part.

We can use the type() function to know which class a variable or a value belongs to.
"""

print(".......... Numeric Data Type ............")

num = 19
print(num, "is of", type(num))

num2 = 19.87
print(num2, "is of", type(num2))

num3 = 3j
print(num3, "is of", type(num3))

"""
Number Systems
The numbers we deal with every day are of the decimal (base 10) number system.

But computer programmers need to work with binary (base 2), hexadecimal (base 16) and octal (base 8) number systems.

In Python, we can represent these numbers by appropriately placing a prefix before that number. 
The following table lists these prefixes.

Number System	    Prefix
Binary	            0b or 0B
Octal	            0o or 0O
Hexadecimal	        0x or 0X
"""
print("\n")
print(".......... Number systems  ............")
print(0b1101011)

print(0xFB + 0b10)

print(0o15)

"""
Type Conversion in Python
In programming, type conversion is the process of converting one type of number into another.

Operations like addition, subtraction convert integers to float implicitly (automatically), 
if one of the operands is float. For example,

print(1 + 2.0) # this will print 3.0
"""

print("\n")
print(".......... Type conversion implicit  ............")

print(1 + 2.3)

print(0.0 + 1)

"""
Explicit Type Conversion
We can also use built-in functions like int(), float() and complex() to convert between types explicitly. 
These functions can even convert from strings.
"""

print("\n")
print(".......... Type conversion Explicit  ............")

print(int(1.2) + 2)

print(complex(2 + 4j))

print(int(3.9) + 5)


"""
Random Module
Python offers the random module to generate random numbers or to pick a random item from an iterator.

First we need to import the random module. For example,

"""

print("\n")
print(".......... Random  ............")

import random

list1 = ['a', 'b', 'c', 'd', 'e']

# get random item from list1
print(random.choice(list1))

# Shuffle list1
random.shuffle(list1)

# Print the shuffled list1
print(list1)

# Print random element
print(random.random())


print(random.randrange(2,5))

names = ['John', 'Mary', 'Micheal', 'Jane']
random.shuffle(names)
print(names)

"""
Mathematics
Python offers the math module to carry out different mathematics like trigonometry, 
logarithms, probability and statistics, etc.
"""

import math

print(math.pi)

print(math.cos(math.pi))

print(math.exp(10))

print(math.log10(1000))

print(math.sinh(1))

print(math.factorial(6))
