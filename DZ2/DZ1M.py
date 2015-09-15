__author__ = 'NikolaiEgorov'
def Lad(a1, a2, b1, b2):
    if (a1 == b1) | (a2 == b2):
        return 'YES'
    else:
        return 'NO'
a1 = int(input())
a2 = int(input())
b1 = int(input())
b2 = int(input())
print(Lad(a1,a2,b1,b2))
