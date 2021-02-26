import math


def initialize(prime, N, value):
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

def isNdigtel(prime):# value=3
    count=[]
    initialize()
    prime[0] = prime[1] = 0
    for i in range(len(prime),2,-1):
        if prime[i]!=0:



prime=[]
initialize(prime,987654321+1)


