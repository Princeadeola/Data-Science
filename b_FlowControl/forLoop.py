"""
Loop
In Python, a for loop is used to iterate over sequences such as lists, strings, tuples, etc.

for loop Syntax
for val in sequence:
    # statement(s)
Here, val accesses each item of the sequence on each iteration. The loop continues until we reach the last item in the sequence.
"""

print("..........Loop Through a list............")
names = ["John", "James", "Jane"]
for i in names:
    print(i)


print("\n")
print("..........Loop Through a String............")
name = "John Doe"
for i in name:
    print(i)


"""
for Loop with Python range()
In Python, the range() function returns a sequence of numbers. For example,

values = range(4)
Here, range(4) returns a sequence of 0, 1, 2 ,and 3.

Since the range() function returns a sequence of numbers, we can iterate over it using a for loop. 
"""

print("\n")
print("..........Loop Through a Python range()............")
for item in range(6):
    print(item)


"""
Nested for loops
A for loop can also have another for loop inside it. For each cycle of the outer loop, the inner 
loop completes its entire sequence of iterations.

# outer loop 
for i in range(2):
    # inner loop
    for j in range(2): 
        print(f"i = {i}, j = {j}")
"""

print("\n")
print("..........Nested for loop............")
age = [12, 13, 4, 5, 3]
for i in age:
    for h in range(5):
        print(f"i = {i}, h = {h}")
