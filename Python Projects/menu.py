# Program to create a menu with the following options:
# 1. TO PERFORM ADDITION +
# 2. TO PERFORM SUBTRACTION -
# 3. TO PERFORM MULTIPLICATION *
# 4. TO PERFORM DIVISION //


# Accepts user input details and performs the operations accordingly.


# 1. TO PERFORM ADDITION +
def add(a, b):
    s = a + b
    print("The sum is:", s)


#  1. TO PERFORM SUBTRACTION -
def subtract(a, b):
    d = a - b
    print("The difference is:", d)


#  1. TO PERFORM MULTIPLICATION *
def multiply(a, b):
    p = a * b
    print("The product is:", p)


#  1. TO PERFORM DIVISION //
def divide(a, b):
    q = a // b
    print("The quotient is:", q)
    

q = 'y'
while (q! = 'q')

print("1. TO PERFORM ADDITION")
print("2. TO PERFORM SUBTRACTION")
print("3. TO PERFORM MULTIPLICATION")
print("4. TO PERFORM DIVISION")


choice = int(input("Enter your choice:"))

a = int(input("Enter the first number:"))
b = int(input("Enter the second number:"))


if choice == 1:
    add(a, b)
elif choice == 2:
    subtract(a, b)
elif choice == 3:
    multiply(a, b)
elif choice == 4:
    divide(a, b)


print("Print q to quit")

q = input("Do you want to continue?")