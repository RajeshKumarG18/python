employees = ["Yashas", "Reddy", "Ganavi", "Samarth", "Abay"]

roles = ["Manager", "Developer", "Designer", "Tester", "HR"]

experience = [2, 5, 3, 1, 4]

for name, role, years in zip(
    employees, roles, experience):  3Z 
    print(f"""{name} works as {role} with {years} years experience.""")


data = [
    ("Yashas", "HR", 5),
    ("Reddy", "Developer", 3),
    ("Ganavi", "Designer", 2),
    ("Samarth", "Tester", 4),
    ("Abay", "Manager", 6)
]

names, roles, years = zip(*data)
print("Names:", names)
print("Roles:", roles)
print("Years of Experience:", years)