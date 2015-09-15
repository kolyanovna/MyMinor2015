__author__ = 'NikolaiEgorov'


def factor(x):
    if x == 0:
        return 1
    else:
        return x * factor(x - 1)


def sochet(n, k):
    return str(int(factor(n) / (factor(k) * factor(n - k))))


n = int(input())
k = int(input())
print(sochet(n, k))
