"""
Python Implicit Type Conversion
In certain situations, Python automatically converts one data type to another.
This is known as implicit type conversion.
"""

integer_number = 5
float_number = 5.6

converted_to_float = integer_number + float_number
print(converted_to_float)
# it was converted to float to avoid data loss, instead of having just 10,
# which means i will be losing the.5, that is why it was all converted to a higher data type float
print(type(converted_to_float))


"""
Explicit Type Conversion
In Explicit Type Conversion, users convert the data type of an object to required data type.

We use the built-in functions like int(), float(), str(), etc to perform explicit type conversion.

This type of conversion is also called typecasting because the user casts (changes) the data type of the objects.

NOTE: In Type Casting, loss of data may occur as we enforce the object to a specific data type.

"""

# Addition of string and integer Using Explicit Conversion
num_string = '24'
num_int = 25

print("The data of num_string before converting is", type(num_string))

num_string = int(num_string)
print("The data type of num_string after converting is", type(num_string))

sum = num_string + num_int
print("sum is", sum)
print("The data type of sum is", type(sum))