__author__ = 'NikolaiEgorov'

def find(arr):
    flag = True
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if (int(arr[i]) == -int(arr[j])):
                flag = False
                return i, j
    return -1, -1

arr = input().split()
(i, j) = find(arr)
if (i != -1):
    print(i, j)
