__author__ = 'NikolaiEgorov'

def SelectionSort(A):
    for i in range(len(A)):
        C = A[findmax(A,i)]
        A[findmax(A,i)] = A[i]
        A[i] = C
    return A

def findmax(A, index):
    Max = A[index]
    maxindex = index
    for j in range (index+1, len(A)):
        if int(A[j]) > int(Max):
            Max = A[j]
            maxindex = j
    return maxindex

arr = input().split()
arr = SelectionSort(arr)
str = ""
for i in range(len(arr)):
   str += arr[i] + " "
print(str.strip())