__author__ = 'NikolaiEgorov'

n = int(input())

sum = 0
for i in range(n):
    sum += i + 1
for i in range(n-1):
    a = int(input())
    sum -= a
print(str(sum))