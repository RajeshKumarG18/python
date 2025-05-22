a = 50
b = 0
c = 100

def range(a, b, c):
    return a < b < c

if range(a, b, c):
    print(f"{b} falls within the given range {a} to {c}")
else:
    print(f"{b} falls within the given range {a} to {c}")