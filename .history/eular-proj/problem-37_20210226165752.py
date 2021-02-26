import math


def initialize(prime, N):
    for i in range(0, N):
        prime.append(-1)
    prime[0] = prime[1] = 0


def isPrime(prime):
    for j in range(2, len(prime)):
        for i in range(2, int(math.pow(j, 0.5)) + 1):
            if prime[i] == 1 and j % i == 0:
                prime[j] = 0
                break
        if prime[j] == -1: prime[j] = 1


def isPerfectPrime(prime):
    for j in range(2, len(prime)):
        if prime[j]==1:
            prime[j] = 2
            i = 10
            while i < j:
                rmd = int(j % i)
                quotient = j // i
                if prime[rmd] == 0 or prime[quotient] == 0:
                    prime[j] = 1
                    break
                i = i * 10


prime = []
initialize(prime, 1000000)
isPrime(prime)
isPerfectPrime(prime)

for i, value in enumerate(prime):
    if value==2: print(i)