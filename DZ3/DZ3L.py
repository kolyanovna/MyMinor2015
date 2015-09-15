__author__ = 'NikolaiEgorov'

a = int(input())
b = int(input())
c = int(input())

if a > b:
    a, b = b, a
if b > c:
    b, c = c, b
elif a > c:
    a, b, c = a, c, b
if a > b:
    a,b = b,a
print(str(a), str(b), str(c), sep = " ")