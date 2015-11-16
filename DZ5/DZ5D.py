__author__ = 'NikolaiEgorov'

f = open('input.txt', 'r')
n = ''
for line in f:
    n += line
f.close()
print(len(set(n.split())))