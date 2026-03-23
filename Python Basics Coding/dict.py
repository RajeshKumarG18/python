# Program to create a dictionary and perform the methods


d = {1:'a', 2:'b', 3:'c', 4:'d', 5:'e', 'tomato':'fruit'}
print(d)
print()

print(d['tomato'])
print(d[1])
print(d[3])
print()

print(d.get('tomato'))
print()

d[3] = 'f'
print(d)
print()

n = len(d)
print("The length of the dictionary is:", n)