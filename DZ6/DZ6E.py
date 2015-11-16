__author__ = 'NikolaiEgorov'


def C(n,k):
    if (k == 0) or (k == n):
        return 1
    else:
        return C(n-1,k-1)+C(n-1,k)

n = int(input())
k = int(input())

print(C(n,k))