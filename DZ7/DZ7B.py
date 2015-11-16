__author__ = 'NikolaiEgorov'

fr = open('input.txt', 'r')
(a,b) = fr.read().split()
a = int(a)
b = int(b)
fr.close()
fw = open('output.txt', 'w')
c = a+b;
fw.write(str(c))
fw.close()