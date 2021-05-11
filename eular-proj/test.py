# import sys
# import stdarray
# import stdio
# n = int(sys.argv[1])
# isPrime = stdarray.create1D(n+1, True)
# for i in range(2,n+1):
#     if isPrime[i]:
#         #Mark multiples of i as nonprime.
#         for j in range(2,n//i+1):
#             isPrime[i*j]=False
# # Count the primes.
# count = 0
# for i in range(2,n+1):
#     if isPrime[i]:
#          count += 1
# stdio.write(count)


from primesieve import *
#primes(100000, 1000000)
print(primes(1000000000, 10000000000))


