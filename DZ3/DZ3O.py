__author__ = 'NikolaiEgorov'

n = int(input())
sum = 0
lastn = 1
for i in range(n):
    lastn *= (i+1)
    sum += lastn

print(str(sum))
