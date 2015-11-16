__author__ = 'NikolaiEgorov'

N = input()
line = input()
x = int(input())
delta = 3000
n = 3000
m = 3000
for i in line.split():
    if (abs(x - int(i)) == delta) and (int(i) != n):
        m = int(i)
    if abs(x - int(i)) < delta:
        delta = abs(x - int(i))
        n = int(i)
        m = 3000
line = str(n)
if (m != 3000):
    line += " " + str(m)
print(line)