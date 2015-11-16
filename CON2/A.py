__author__ = 'NikolaiEgorov'

N = input()
line = input()
x = int(input())
n = 0
for i in line.split():
    if x == int(i):
        n += 1
print(n)
