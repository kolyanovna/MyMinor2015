__author__ = 'NikolaiEgorov'

(n,m,k) = input().split()
n = int(n)
m = int(m)
k = int(k)
arr = []
arr2 = []
for i in range(k):
    arr2.append([0, 0, 0, 0])
for i in range(n):
    arr.append(input().split())

for i in range(k):
    xy = input().split()
    for j in range(4):
        arr2[i][j] = int(xy[j])
for i in range(k):
    x1 = arr2[i][0]
    y1 = arr2[i][1]
    x2 = arr2[i][2]
    y2 = arr2[i][3]
    sum = 0
    for mas in arr[x1-1:x2]:
        for num in mas[y1-1:y2:]:
            sum += int(num)
    print(sum)

