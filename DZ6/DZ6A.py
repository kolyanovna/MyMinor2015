__author__ = 'NikolaiEgorov'


def min4(a, b, c, d):
    return min(a, min(b, min(c, d)))

a = int(input())
b = int(input())
c = int(input())
d = int(input())
print(min4(a, b, c, d))


