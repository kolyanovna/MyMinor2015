__author__ = 'NikolaiEgorov'

s = input().split()
for i in range(len(s)):
    if i % 2 == 0 and (i+1 < len(s)):
        (s[i], s[i+1]) = (s[i+1], s[i])
strok = ""
for i in range(len(s)):
    strok += s[i] + " "
print(strok)