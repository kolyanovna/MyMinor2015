__author__ = 'NikolaiEgorov'

def IsAscendig(A):
    arr = A.split()
    last = int(arr[0])
    flag = True
    i = 0
    while (bool and i < len(arr)-1):
        i += 1
        new = int(arr[i])
        if (last >= new):
            flag = False
        last = new
    if (len(arr)-1 == i and flag):
        return('YES')
    else:
        return('NO')

str = input()
print(IsAscendig(str))


