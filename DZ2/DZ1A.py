__author__ = 'NikolaiEgorov'
x = 2
n = 179
def mypow(xx, nn):
    ans = 1
    while nn > 0:
        if nn % 2 == 1:
            ans *= xx
        xx *= xx
        nn >>= 1
    return ans

print(str(mypow(x, n)))

