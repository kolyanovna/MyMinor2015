__author__ = 'NikolaiEgorov'

N = input()
line = input()
min1 = 2000000001
min2 = 2000000001
for i in line.split():
    if min1 > int(i):
        if min2 > int(i):
            min1 = min2
            min2 = int(i)
        else:
            min1 = int(i)
print(str(min2) + " " + str(min1))