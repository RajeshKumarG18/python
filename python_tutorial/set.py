# Creating a set
my_set = {1, 2, 3, 4, 2}
print(my_set) # Output: {1, 2, 3, 4} (duplicates are removed)

# Adding an element
my_set.add(5)
print(my_set) # Output: {1, 2, 3, 4, 5}

# Removing an element
my_set.remove(3)
print(my_set) # Output: {1, 2, 4, 5}

# Set operations
set_a = {1, 2, 3}
set_b = {3, 4, 5}

union_set = set_a | set_b
print(union_set) # Output: {1, 2, 3, 4, 5}

intersection_set = set_a & set_b
print(intersection_set) # Output: {3}