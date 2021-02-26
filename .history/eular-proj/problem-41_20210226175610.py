import math


def initialize(prime, N, value):
    # prime = [value for i in range(N)]
    prime = [value] * N
    prime[0] = prime[1] = 0
    return prime


def isPrime(prime):
    for j in range(2, len(prime)):
        for i in range(2, int(math.pow(j, 0.5)) + 1):
            if prime[i] == 1 and j % i == 0:
                prime[j] = 0
                break
        if prime[j] == -1: prime[j] = 1


def isNdigtel(prime):
    count = []
    count=initialize(count, 10, 0)
    for i in range(len(prime)-1, 2, -1):
        if prime[i] != 0:
            prime[i] = 3
            num = str(i)
            for l in num:
                count[int(l)] = count[int(l)] + 1
                if count[int(l)] > 1:
                    prime[i] = 1
                    break
            if prime[i] == 3: break


prime = []
prime=initialize(prime, 98765 + 1, -1)
isPrime(prime)
isNdigtel(prime)
for i, value in enumerate(prime):
    if value==1: print(i)
