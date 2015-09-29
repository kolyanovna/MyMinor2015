__author__ = 'NikolaiEgorov'

strok = input().split('@')
newstrok = ""
for i in range(len(strok)):
    newstrok += strok[i]
print(newstrok)