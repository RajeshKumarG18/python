# Can you compute all multiples of 3, 5
# that are less than 100
# print(list(range(1, 100)))

limit = 100
multiples = []
for i in range(limit):
        if i % 3 == 0 and i % 5 == 0:
            multiples.append(i)
print(multiples)