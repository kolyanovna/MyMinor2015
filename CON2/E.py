__author__ = 'NikolaiEgorov'


def lftbin(el, arr):
    if el > arr[len(arr) - 1] or el < arr[0]:
        return 0
    lft = 0
    rgt = len(arr) - 1
    while rgt > lft:
        med = int((rgt + lft) / 2)
        if el <= arr[med]:
            rgt = med
        else:
            lft = med + 1
    if arr[lft] == el:
        return lft+1
    else:
        return 0


def rgtbin(el, arr):
    if el > arr[len(arr) - 1] or el < arr[0]:
        return 0
    lft = 0
    rgt = len(arr) - 1
    while rgt > lft+1:
        med = int((rgt + lft) / 2)
        if el < arr[med+1]:
            rgt = med
        else:
            lft = med
    if arr[rgt] == el:
        return rgt+1
    if arr[lft] == el:
        return lft+1
    else:
        return 0


(N, K) = input().split()
arr1 = [int(x) for x in input().split()]
arr2 = [int(x) for x in input().split()]

for i in arr2:
    lft = lftbin(i, arr1)
    if lft != 0:
        print(str(lft)+" "+str(rgtbin(i, arr1)))
    else:
        print(str(lft))
