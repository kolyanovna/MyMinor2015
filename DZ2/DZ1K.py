__author__ = 'NikolaiEgorov'
def Max(a, b, c):
    if a >= b :
        max = a
    else:
        max = b
    if c > max :
        max = c
    return max
a = int(input())
b = int(input())
c = int(input())
print(str(Max(a, b, c)))

