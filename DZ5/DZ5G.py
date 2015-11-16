__author__ = 'NikolaiEgorov'
f = open('input.txt', 'r')
strok = ''
for line in f:
    strok += line
mas = strok.split()
d = dict.fromkeys(set(mas))
strok = ""
for i in range(len(mas)):
    if d[mas[i]] is not None:
        strok += str(d[mas[i]]) + " "
        d[mas[i]] += 1
    else:
        strok += "0" + " "
        d[mas[i]] = 1
print (strok)
f.close()