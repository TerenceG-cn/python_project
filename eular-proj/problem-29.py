import math

ab = set()
for a in range(2, 101):
    for b in range(2, 101):
        ab.add(math.pow(a, b))
ab = list(ab)
ab.sort()

print(len(ab))