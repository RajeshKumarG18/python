"""
converting from one type to another with the int(), float(), and complex() methods:
"""


x = 18   # int
y = 2.18  # float
z = 18j   # complex

# converting from int to float:
a = float(x)

# converting from float to int:
b = int(y)

# converting from int to complex:
c = complex(x)

print(a)
print(b)
print(c)


'''
To verify the type of any object in Python, using the type() function:
'''

print(type(a))
print(type(b))
print(type(c))