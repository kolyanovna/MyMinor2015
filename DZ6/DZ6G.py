__author__ = 'NikolaiEgorov'


def reverse(N, str):
    num = str[0:str.index(" ")+1]
    str = str[str.index(" ")+1:]
    if N != 1:
        return reverse(N - 1, str) + num
    else:
        return num

N = int(input())
str = input()
print(reverse(N, str + " ").strip())
