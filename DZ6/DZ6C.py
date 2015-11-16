__author__ = 'NikolaiEgorov'
import math
def power(a, n):
    if n != 0:
        return float(a*power(a,n-1))
    else:
        return 1

a = float(input())
n = int(input())

a = power(a, n)
if math.modf(a) == (0, int(a)):
    print(int(a))
else:
    print(float(a))
