__author__ = 'NikolaiEgorov'

strok = input().split()
min = strok[0]
minin = 0;
max = strok[0]
maxin = 0;
for i in range(1, len(strok)):
    if int(strok[i]) > int(max):
        max = strok[i]
        maxin = i
    if int(strok[i]) < int(min):
        min = strok[i]
        minin = i
strok[maxin], strok[minin] = strok[minin], strok[maxin]
s = ""
for i in range(len(strok)):
    s += strok[i] + " "
print(s)
