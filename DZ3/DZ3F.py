__author__ = 'NikolaiEgorov'


def canornot(n, m, k):
    num = []
    for i in range(n):
        for j in range(m):
            if num.count((i + 1) * (j + 1)) == 0:
                num.append((i + 1) * (j + 1))
    if num.count(k) == 0:
        print("NO")
    else:
        print("YES")

n = int(input())
m = int(input())
k = int(input())

canornot(n, m, k)
