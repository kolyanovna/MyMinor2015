__author__ = 'NikolaiEgorov'

n = int(input())
dict = {}
for i in range(n):
    s = input().split()
    a = s[0]
    for j in range(1, len(s)):
        dict[s[j]] = a
m = int(input())
strok = ""
for i in range(m):
    strok += (dict[input()]) + "\n"
print(strok)