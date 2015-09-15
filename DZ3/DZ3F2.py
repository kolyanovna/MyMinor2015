__author__ = 'NikolaiEgorov'


# метод нахождения наибольшнго общего делителя
def NOD(a, b):
    while True:
        if a > b:
            a -= b
        elif b > a:
            b -= a
        else:
            return int(a)


# метод находящий состовляют ли какие-нибудь числа меньше n и m в произведении k
def canornot(n, m, k):
    maxdel = 0;
    if n >= m:
        for i in range(n):
            if NOD(i+1, k) > maxdel:
                maxdel = NOD(i+1, k)
        if k / maxdel <= m:
            print("YES")
        else:
            print("NO")
    else:
        for i in range(m):
            if NOD(i+1, k) > maxdel:
                maxdel = NOD(i+1, k)
        if k / maxdel <= n:
            print("YES")
        else:
            print("NO")


n = int(input())
m = int(input())
k = int(input())

canornot(n, m, k)
