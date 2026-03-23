# Program to create a tuple & perform the methods


tuple = (1, 2, 3, 4, 5, 6, 7, 8)
print("The original tuple is:", tuple)


tuple = tuple + (9, 10)
print(tuple)


n = len(tuple)
print("The length of tuple is:", n)


pos = tuple.index(4)
print("The position of 4, in tuple is:", pos)
print(tuple[4])
print(tuple[2])
print(tuple[3])