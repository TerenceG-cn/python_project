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
size=12001
count=0
for denominator in range(1,size):
    for numerator in range(math.floor(denominator/3),math.ceil(denominator/2)):
        if gcd(denominator,numerator)==1 and numerator*3>denominator and numerator*2<denominator:
            count+=1
print(count)

