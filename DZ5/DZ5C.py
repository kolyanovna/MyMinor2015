__author__ = 'NikolaiEgorov'

s = set()
for i in input().split():
    if not i in s:
        s.add(i)
        print('NO')
    else:
        print('YES')

