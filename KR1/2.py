__author__ = 'NikolaiEgorov'

n = [0, 0, 0]
n[0] = int(input())
n[1] = int(input())
n[2] = int(input())
s = 0
for i in range(3):
    if n[i] % 2 == 0:
        s += n[i]/2
    else:
        s += int(n[i]/2)+1
print(int(s))
