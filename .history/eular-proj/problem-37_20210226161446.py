import math
prime = []
for i in range(0, 1000000):
    prime.append(-1)
prime[0] = prime[1] = 0


def isPrime(num, prime):
    if num < len(prime) and prime[num] != -1: return prime[num]

    for i in range(2, int(math.pow(num, 0.5))):
        if prime[i] == 1 and num % i == 0: prime[num] = 0


isPrime(100, prime[100])
print(prime)