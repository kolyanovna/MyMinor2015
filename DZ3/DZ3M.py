__author__ = 'NikolaiEgorov'


def bil2(n):
    if n % 10 != 0:
        if bil1(n % 10) < 125:
            return bil2((n // 10) * 10) + bil1(n % 10)
        else:
            return 125 * (n//10+1)
    else:
        return 125 * n / 10


def bil1(n):
    return 15 * n


n = int(input())
a1 = 0
a2 = 0
a3 = 0

a3 = n // 60
if int(bil2(n - a3 * 60)) < 440:
    if bil1((n - a3*60) % 10) < 125:
        a2 = (n - a3*60) // 10
        a1 = (n - a3*60) % 10
    else:
        a2 = (n - a3*60) // 10 + 1
else:
    a3 += 1

print(a1, a2, a3, sep=' ')
