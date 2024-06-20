"""
 List
We create a list by placing elements inside square brackets [], separated by commas. For example,

 # a list of three elements
ages = [element1, element2, element3, ...]

Note:
    in Python, lists can store data of different data types.
    We can use the built-in list() function to convert other iterables (strings, dictionaries, tuples, etc.) to a list.
    Each element in a list is associated with a number, known as a index. (The index always starts from 0.
    The first element of a list is at index 0, the second element is at index 1, and so on.)


List Characteristics
Lists are:

Ordered - They maintain the order of elements.
Mutable - Items can be changed after creation.
Allow duplicates - They can contain duplicate values.

"""
print(".......... Accessing Lists  ............")

Names = ['John', 'James', 'Jane', 'Joe']
print("Names are", Names)
print("Positive index starts from zero so Names[3] will be:  ", Names[3])
print("Negative index starts from first element in the end, so Names[-1] will be:  ", Names[-1])


print("\n")
print(".......... Appending Lists  ............")
print("Names before appending: ", Names)
Names.append('Joy')
print("Names after appending: ", Names)

Names.insert(2, "June")
print("After adding specific index: ", Names)



print("\n")
print(".......... Changing Lists  ............")
print("Name List before changing: ", Names)
Names[1] = "Joanna"
print("Name List after changing a particular index: ", Names)


print("\n")
print(".......... Other Methods in Lists  ............")
Names.remove("John")
print(Names)
Names.pop(3)
print(Names)


print("\n")
print(".......... Iterating Through a List  ............")

for i in Names:
    print(i)



print("\n")
print(".......... Try this ............")
numbers = [n**2 for n in range(1, 6)]
print(numbers)

print(50 in numbers)
print(1 in numbers)