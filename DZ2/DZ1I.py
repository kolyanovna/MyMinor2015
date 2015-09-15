__author__ = 'NikolaiEgorov'
from math import sqrt
def gipot(a, b):
    return(sqrt(a**2+b**2))
a = int(input())
b = int(input())
print(str(gipot(a, b)))