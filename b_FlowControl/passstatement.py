"""
pass Statement
In Python programming, the pass statement is a null statement
which can be used as a placeholder for future code.

Suppose we have a loop or a function that is not implemented yet, but we want to implement
it in the future. In such cases, we can use the pass statement.

The syntax of the pass statement is:

pass
"""

# Using pass With Conditional Statement
n = 10

# use pass inside if statement
if n > 10:
    pass

print('Hello')


# Use of pass Statement inside Function or Class
# We can do the same thing in an empty function or class as well. For example,
def function(args):
    pass
class Example:
    pass
