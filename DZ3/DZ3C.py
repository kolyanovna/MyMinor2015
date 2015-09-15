__author__ = 'NikolaiEgorov'


def factor(x):
    if x == 0:
        return 1
    else:
        return x * factor(x - 1)

n = int(input())
print(str(factor(n)))

