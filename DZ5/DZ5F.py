__author__ = 'NikolaiEgorov'

f = open('input.txt', 'r')
n = int(f.readline())
a = []
for i in range(n):
    a.append([])
    m = int(f.readline())
    for j in range(m):
        a[i].append(str(f.readline()).strip())
s1 = set(a[0])
s2 = set(a[0])
for i in range(1, n):
    s1 = s1.intersection(set(a[i]))
    s2 = s2.union(set(a[i]))

print(len(s1))
s1 = list(s1)
for i in range(len(s1)):
    print(s1[i])
print(len(s2))
s2 = list(s2)
for i in range(len(s2)):
    print(s2[i])
f.close()