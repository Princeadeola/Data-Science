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