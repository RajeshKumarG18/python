"""
Using the global keyword to modify a variable outside of the current scope.
"""


def myfunc():
  
  global x
  
  x = "programming language"

myfunc()

print("JavaScript is a " + x)