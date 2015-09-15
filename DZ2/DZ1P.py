__author__ = 'NikolaiEgorov'
from math import fabs
def Kon(a1, a2, b1, b2):
    if ((fabs(a1 - b1) == 2) and (fabs(a2 - b2) == 1)) or ((fabs(a1 - b1) == 1) and (fabs(a2 - b2) == 2)):
        return 'YES'
    else:
        return 'NO'
a1 = int(input())
a2 = int(input())
b1 = int(input())
b2 = int(input())
print(Kon(a1,a2,b1,b2))