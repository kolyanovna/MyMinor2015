__author__ = 'NikolaiEgorov'
s = [];
fr = open('input.txt', 'r')
t = fr.readline()
while (t != ""):
    s.append(t)
    t = fr.readline()
fr.close()
fw = open('output.txt', 'w')
s = s[::-1]
for i in range(len(s)):
    fw.write(s[i])
fw.close()