__author__ = 'NikolaiEgorov'

import math
def IsPrime(n):
    if n in (1, 2, 3):
        return True
    else:
        for i in range(2, int(math.sqrt(n))+1):
            if n % i == 0:
                return False
        return True

n = int(input())
if IsPrime(n):
    print('YES')
else:
    print('NO')
