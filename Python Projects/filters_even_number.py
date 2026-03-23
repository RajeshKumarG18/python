# Program to filter() the even numbers from the list elements




def even(value):
    if value % 2 == 0:
        return True
    else:
        return False
li = eval(input("Enter a list:"))
filtered = filter(even, li)
for i in filtered:
    print(li)