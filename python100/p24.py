a = 1
b = 2
s = 0

for n in range(1, 21):
    s += b / a
    t = b
    b = a + b
    a = t
print(s)

a1 = 1.0
b1 = 2.0
s1 = 0.0

for n in range(1, 21):
    s1 += b1 / a1
    a1, b1 = b1, a1 + b1
print(s1)

from functools import reduce

a2 = 1.0
b2 = 2.0
l = []

for n in range(1, 21):
    l.append(b2 / a2)
    a2, b2 = b2, a2 + b2
print(reduce(lambda x, y: x + y, l))
