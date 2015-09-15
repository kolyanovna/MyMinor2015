__author__ = 'NikolaiEgorov'
def Max(a, b):
    if a > b:
        return 1
    elif a == b:
        return 0
    else:
        return 2
a = int(input())
b = int(input())
print(str(Max(a, b)))