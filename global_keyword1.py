"""
To change the value of a global variable inside a function, refer to the variable by using the global keyword.
"""


x = "programming language"

def myfunc():
  
  global x

  x = "easy to learn"

myfunc()

print("Python is " + x)