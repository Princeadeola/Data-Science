"""
Sets
A set is a collection of unique data, meaning that elements within a set cannot be duplicated.

For instance, if we need to store information about student IDs,
a set is suitable since student IDs cannot have duplicates.

Create a Set
In Python, we create sets by placing all the elements inside curly braces {}, separated by commas.

A set can have any number of items, and they may be of different types (integer, float, tuple,
string, etc.). But a set cannot have mutable elements like lists, sets or dictionaries as its elements.

Empty Set in Python
Creating an empty set is a bit tricky. Empty curly braces {} will make an empty dictionary in Python.

To make a set without any elements, we use the set() function without any argument. For example,

# create an empty set
empty_set = set()

# create an empty dictionary
empty_dictionary = { }
"""

print(".......... Creating a set ............")
student_ids = {121, 122, 123, 124, 125}
print("Student IDs: ", student_ids)

mixed_data = {"John", 24, "James", 24, 21, 'o'}
print("Mixed Data: ", mixed_data)


print("\n")
print(".......... Duplicates in Set ............")
duplicates = {21, 23, 25, 21, 3, 7}
print("Duplicates: ", duplicates)


print("\n")
print(".......... Methods in Set ............")

student_ids.add(126)
print("Student IDs: ", student_ids)

student_name = ["John", "James", "Jane", 123]
student_ids.update(student_name)
print("Student Ids after update: ",student_ids)

student_ids.remove(126) # even though remove method worked, it is not part of set methods, use discard instead
print("Student IDs after removing 126: ", student_ids)
student_ids.discard("John")
print("Student IDs after discarding John: ", student_ids)

print("Set length is", len(student_ids))

print("\n")
print(".......... Iterate over a Set ............")
for student in student_ids:
    print(student)


"""
Set Operations
Python Set provides different built-in methods to perform mathematical 
set operations like union, intersection, subtraction, and symmetric difference.
"""


print("\n")
print(".......... Set Operations (union) ............")
"""
Union of Two Sets
The union of two sets A and B includes all the elements of sets A and B.

We use the | operator or the union() method to perform the set union operation. 
"""

setA = {1, 2, 3, 4, 5}
setB = {'John','James', 'Jane', 'Joe'}

print("Union using |: ", setA|setB)
print("Union using union method: ", setA.union(setB))


print("\n")
print(".......... Set Operations (Intersections) ............")
"""
The intersection of two sets A and C include the common elements between set A and C.

In Python, we use the & operator or the intersection() method to perform the set intersection operation.
"""
setC = {1, 3, 4, 6, 'John', 'James'}
print("Intersection using &: ", setC & setA)
print("Intersection using the method: ", setA.intersection(setC))


print("\n")
print(".......... Set Operations (Difference) ............")
"""
Difference between Two Sets
The difference between two sets A and D include elements of set A that are not present on set D.

We use the - operator or the difference() method to perform the difference between two sets. 
"""

setD = {1, 2, 7, 9, 5}
print("Difference using - : ", setA - setD)
print("Difference using the difference method: ", setA.difference(setD))


print("\n")
print(".......... Set Operations (Symmetric Difference) ............")
"""
Symmetric Difference
The symmetric difference between two sets A and D includes all elements of A and D without the common elements.

In Python, we use the ^ operator or the symmetric_difference() method to perform symmetric differences between two sets. 
"""

print("Symmetric difference using ^: ", setA ^ setD)
print("Symmetric difference using the method: ", setA.symmetric_difference(setD))


print("\n")
print(".......... Other methods and conditions Set ............")

if setA == setD:
    print("Both sets are equal")
else:
    print("None equal sets")