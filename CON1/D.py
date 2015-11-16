__author__ = 'NikolaiEgorov'

def InsetionSort(A):
    for i in range(1, len(A)):
        con = A[i]
        for j in range(i-1, -1, -1):
            if int(con) < int(A[j]):
               A[j+1] = A[j]
            else:
                A[j+1] = con
                break
            if (j == 0):
                A[j] = con

arr = input().split()
InsetionSort(arr)
str = ""
for i in range(len(arr)):
   str += arr[i] + " "
print(str.strip())


