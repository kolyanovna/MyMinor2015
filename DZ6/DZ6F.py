__author__ = 'NikolaiEgorov'


def sum(n, m):
    if m == 0:
        return n
    else:
        return sum(n + 1, m - 1)


n = int(input())
m = int(input())

print(sum(n, m))
