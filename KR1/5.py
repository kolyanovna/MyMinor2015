__author__ = 'NikolaiEgorov'

a = int(input())
b = int(input())
s = [0, 0, 0, 0]
for i in range(a, b+1):
    n = i
    for j in range(4):
        s[j] = (n % 10)
        n = int(n / 10)
    for y in range(2):
        sum = 0
        for k in range(y, 4):
            if s[y] == s[k]:
                sum += 1
        if sum == 4:
            break
        if sum == 3:
            print (str(i))
