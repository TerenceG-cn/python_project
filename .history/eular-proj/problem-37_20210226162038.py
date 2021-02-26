import math
prime = []
for i in range(0, 1000000):
    prime.append(-1)
prime[0] = prime[1] = 0


def isPrime(prime):
    for j in range(2,len(prime)):
        for i in range(2, int(math.pow(num, 0.5))+1):
            if prime[i] == 1 and j % i == 0: prime[j] = 0
        


isPrime(100, prime)
print(prime[1000000-1])