__author__ = 'NikolaiEgorov'
a = 0
b = 0
strok = input()
bool = False
for i in range(len(strok)):
    if bool:
        if strok[i] == "f":
            b = i
    else:
        if strok[i] == "f":
            a = i
            bool = True
if (a == 0) and (b == 0):
    pass
else:
    if (b != 0):
        s = str(a)+" "+str(b)
        print(s)
    else:
        print(a)