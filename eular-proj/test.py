import primesieve
import math
#print(primesieve.n_primes(math.pow(10,5)))

#help(primesieve)

import primesieve

it = primesieve.Iterator()
prime = it.next_prime()

# Iterate over the primes below 10000
# while prime < 10000:
#     print(prime)
#     prime = it.next_prime()

# Set iterator start number to 100
it.skipto(int(math.pow(10,14)))
prime1 = it.next_prime()
prime2 = it.next_prime()
print(prime1,prime2)

# Iterate backwards over the primes below 100
# while prime > 0:
#     print(prime)
#     prime = it.prev_prime()

