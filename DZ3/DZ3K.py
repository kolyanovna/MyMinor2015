__author__ = 'NikolaiEgorov'
n = int(input())
for i in range(n):
    n = ""
    for j in range(i+1):
        n += str(j+1)
    print(n)