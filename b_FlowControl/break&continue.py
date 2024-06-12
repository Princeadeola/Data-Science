"""
break and continue
In programming, the break and continue statements are used to alter the flow of loops:

break exits the loop entirely
continue skips the current iteration and proceeds to the next one
"""

"""
break Statement
The break statement terminates the loop immediately when it's encountered.

Syntax is break
"""

print("..........Break keyword............")
for i in range(5):
    if i == 3:
        break
    print(i)

"""
continue Statement
The continue statement skips the current iteration of the loop and 
the control flow of the program goes to the next iteration.
"""
print("\n")
print("..........continue keyword............")

for i in range(5):
    if i == 3:
        continue
    print(i)
