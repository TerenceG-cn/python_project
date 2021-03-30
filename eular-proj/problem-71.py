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
import math
size=1000001
r_n=1
r_d=size
for denominator in range(1,size):
    for numerator in range(math.floor(denominator*r_n/r_d),math.ceil(denominator*3/7)):
        if gcd(denominator,numerator)==1 and numerator*r_d>r_n*denominator and numerator*7<3*denominator:
            r_n=numerator
            r_d=denominator
print(r_n,r_d)

