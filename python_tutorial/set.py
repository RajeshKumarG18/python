# Creating a set
my_set = {1, 2, 3, 4, 2}
print(my_set) # Output: {1, 2, 3, 4} (duplicates are removed)

# Adding an element
my_set.add(5)
print(my_set) # Output: {1, 2, 3, 4, 5}

# Removing an element
my_set.remove(3)
print(my_set) # Output: {1, 2, 4, 5}


# Checking membership
# Set operations
set_a = {1, 2, 3}
set_b = {3, 4, 6, 5}

union_set = set_a | set_b
print(union_set) # Output: {1, 2, 3, 4, 5}

intersection_set = set_a & set_b
print(intersection_set) # Output: {3}

# To make the set item in order or arrange in order the items or numbers, for that we use List method to arrange in order in set in python.
my_set = {1, 2, 3, 4, 5}
ordered_set = sorted(my_set)
print(ordered_set) # Output: [1, 2, 3, 4, 5]
# Checking if a set is a subset of another
a = {1, 2}
b = {1, 2, 3, 4}
print(a.issubset(b))   # Output: True
# Checking if a set is a superset of another
print(b.issuperset(a))   # Output: True
# Checking if two sets are disjoint
c = {5, 6}
print(a.isdisjoint(c))   # Output: True
# Set comprehension
squared_set = {x**2 for x in range(5)}
print(squared_set) # Output: {0, 1, 4, 9, 16}
# Converting a list to a set to remove duplicates
my_list = [1, 2, 2, 3, 4]
unique_set = set(my_list)
print(unique_set) # Output: {1, 2, 3, 4}
# Using the pop method to remove an arbitrary element
my_set = {1, 2, 3, 4}
popped_value = my_set.pop()
print(popped_value) # Output: 1 (or any other element, as sets are
# unordered)
print(my_set) # Output: {2, 3, 4} (the popped element is removed)
# Using the clear method to remove all elements from a set
my_set = {1, 2, 3, 4}
my_set.clear()
print(my_set) # Output: set() (the set is now empty)
# Using the copy method to create a shallow copy of a set
original_set = {1, 2, 3}
copied_set = original_set.copy()
print(copied_set) # Output: {1, 2, 3}