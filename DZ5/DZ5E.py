__author__ = 'NikolaiEgorov'

f = open('input.txt', 'r')
(n, m) = f.readline().split()
n = int(n)
m = int(m)
a = []
b = []
for i in range(n):
    a.append(int(f.readline()))
for i in range(m):
    b.append(int(f.readline()))
s = set(a).intersection(set(b))
print(len(s))
strok = ''
a.sort()
b.sort()
for i in range(n):
    if a[i] in s:
        strok += str(a[i])+' '
print(strok.strip())
s = set(a).difference(b)
print(len(s))
strok = ''
for i in range(n):
    if a[i] in s:
        strok += str(a[i])+' '
print(strok.strip())
s = set(b).difference(a)
print(len(s))
strok = ''
for i in range(m):
    if b[i] in s:
        strok += str(b[i])+' '
print(strok.strip())
f.close()
