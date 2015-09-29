__author__ = 'NikolaiEgorov'
strok = input()
newstrok = ""
for i in range(len(strok)-1):
    newstrok += strok[i] + '*'
newstrok += strok[len(strok)-1]
print(newstrok)
