__author__ = 'NikolaiEgorov'

def BubbleSort(A):
    for i in range(len(A)):
        for j in range(len(A)-i-1):
            if int(A[j]) < int(A[j+1]):
                (A[j+1], A[j]) = (A[j], A[j+1])

arr = input().split()
BubbleSort(arr)
str = ""
for i in range(len(arr)):
   str += arr[i] + " "
print(str.strip())