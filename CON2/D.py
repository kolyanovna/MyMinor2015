__author__ = 'NikolaiEgorov'


(N, K) = input().split()
arr1 = [int(x) for x in input().split()]
arr2 = [int(x) for x in input().split()]
for i in arr2:
    if i > arr1[len(arr1)-1] or i < arr1[0]:
        print("NO")
        continue
    lft = 0
    rgt = len(arr1)-1
    while rgt > lft:
        med = int((rgt+lft)/2)
        if i <= arr1[med]:
            rgt = med
        else:
            lft = med+1
    if arr1[rgt] == i:
        print("YES")
    else:
        print("NO")
