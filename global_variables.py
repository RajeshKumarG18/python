"""
1. Create a variable outside of a function, and use it inside the function.
"""


x = "programming language"

def myfunc():

    print("Python is a " + x)

myfunc()