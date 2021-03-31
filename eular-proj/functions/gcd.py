def gcd(a, b):
    if a < b:
        a, b = b, a
    if a == 0 and b == 0:
        return 0
    while b != 0:
        c = a % b
        a = b
        b = c
    return a