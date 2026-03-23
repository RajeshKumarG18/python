"""
Create a variable inside a function, with the same name as the global variable.
"""


x = "programming language"

def myfunc():
    x = "easy to learn"

    print("Python is " + x)

myfunc()

print("Python is a " + x)