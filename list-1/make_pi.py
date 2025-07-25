# Return an int array length 3 containing the first 3 digits of pi, {3, 1, 4}.

# make_pi() → [3, 1, 4]

def make_pi():
    pi = []
    ele = [3, 1, 4]
    for i in ele:
        if i in ele:
            pi.append(i)
    return pi