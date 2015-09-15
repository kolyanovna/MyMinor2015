__author__ = 'NikolaiEgorov'


def pinguinsprint(n):
    pinguin = ("   _~_   ", "  (o o)  ", " /  V  \ ", "/(  _  )\\", "  ^^ ^^  ")
    for i in range(5):
        strok = ""
        for j in range(n):
            strok += pinguin[i]
            if j != n - 1:
                strok += " "
        print(strok)

n = int(input())
pinguinsprint(n)