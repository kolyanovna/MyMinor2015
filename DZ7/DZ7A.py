__author__ = 'NikolaiEgorov'

fr = open('input.txt', 'r')
a = int(fr.readline())
b = int(fr.readline())
fr.close()
fw = open('output.txt', 'w')
c = a+b;
fw.write(str(c))
fw.close()