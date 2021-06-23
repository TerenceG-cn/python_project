import math
import primesieve
from functions import eular_func
# n 强大的（似幂的），如果对n的每一个质因数p，p^2都是n的约数
def is_powerful(n):
    for p in primesieve.primes(n):
        if n%p==0 and n%int(math.pow(p,2))!=0:
            return False
    return True
# n 完美的（完全幂的）
def is_perfect(n):
    eval=int(math.sqrt(n))
    return int(math.pow(eval,2))== n
# n Achilles
def is_achilles(n):
    return is_powerful(n) and not is_perfect(n)

import eulerlib
e = eulerlib.numtheory.Divisors(10000) # 这里的10000是最大值，默认是1000
def is_strong_achilles(n):
    return is_achilles(n) and is_achilles(int(e.phi(n)))

count=0
for n in range(1,int(math.pow(10,8))):
    if is_strong_achilles(n):
        #print(n)
        count+=1
print(count)
# 216
# 500
# 648
# 864
# 1944
# 2000
# 2592
# 3375
# 3456
# 5000
# 5832
# 7776
# 8000
# 9261