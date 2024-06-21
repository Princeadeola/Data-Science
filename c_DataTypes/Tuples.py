"""
Tuple
A tuple is a collection similar to a Python list. The primary difference is
that we cannot modify a tuple once it is created.

Create a Python Tuple
We create a tuple by placing items inside parentheses ().

Tuples are:

Ordered - They maintain the order of elements.
Immutable - They cannot be changed after creation.
Allow duplicates - They can contain duplicate values.
Access Tuple Items
Each item in a tuple is associated with a number, known as a index.

The index always starts from 0, meaning the first item of a tuple
is at index 0, the second item is at index 1, and so on.
"""

print(".......... Tuple  ............")
ages = (21, 30, 23, 18)
print(ages)

print("\n")
print(".......... Tuple using construct ............")
number_using_construct = tuple((2, 3, 1, 7, 5))
print(number_using_construct)

print("\n")
print(".......... Tuple Iteration ............")
for age in ages:
    print(age)

print("\n")
print(".......... Tuple Methods ............")
print(len(number_using_construct))

print(2 in number_using_construct)
