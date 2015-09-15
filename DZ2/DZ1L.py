__author__ = 'NikolaiEgorov'
def Trian(a, b, c):
    if (a + b > c) & (a + c > b) & (b + c > a):
        return 'YES'
    else:
        return 'NO'
    return max
a = int(input())
b = int(input())
c = int(input())
print(Trian(a, b, c))