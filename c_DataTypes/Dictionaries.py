"""
Dictionary
A Python dictionary is a collection of items, similar to lists and tuples.
However, unlike lists and tuples, each item in a dictionary is a key-value pair (consisting of a key and a value).

Create a Dictionary
We create a dictionary by placing key: value pairs inside curly brackets {}, separated by commas.

NOTE:
Dictionary keys must be immutable, such as tuples, strings, integers, etc.
We cannot use mutable (changeable) objects such as lists as keys.
We can also create a dictionary using a Python built-in function dict().
"""

print(".......... Creating a Dictionary ............")
users_info = {"John": 21, "James": 24, "Joe": 26, "Jane": 22}
print("Current dictionary: ", users_info)

"""
Keys of a dictionary must be immutable
Immutable objects can't be changed once created. Some immutable objects in Python are integer, tuple and string.

for example, we have used integers, tuples, and strings as keys for the dictionaries. 
When we used a list as a key, an error message occurred due to the list's mutable nature.

Note: Dictionary values can be of any data type, including mutable types like lists.
"""
# valid dictionary
# integer as a key
my_dict = {1: "one", 2: "two", 3: "three"}

# valid dictionary
# tuple as a key
my_dict2 = {(1, 2): "one two", 3: "three"}

# invalid dictionary
# Error: using a list as a key is not allowed
# my_dict3 = {1: "Hello", [1, 2]: "Hello Hi"}

# valid dictionary
# string as a key, list as a value
my_dict4 = {"USA": ["Chicago", "California", "New York"]}



print("\n")
print("..........Methods in Dictionary ............")

print("Access user: ", users_info["Joe"])

users_info["Joel"] = 28
print("After adding new user: ", users_info)

del users_info["Joel"]
print("After deleting user: ", users_info)

users_info["Joe"] = 27
print("After changing an user value: ", users_info)



print("\n")
print("..........printing keys in Dictionary ............")
for user_key in users_info:
    print(user_key)



print("\n")
print("..........Printing values in Dictionary ............")
for user_value in users_info:
    values = users_info[user_value]
    print(values)