__author__ = 'NikolaiEgorov'


fr = open('input.txt', 'r')
s = fr.read()
fr.close()
fw = open('output.txt', 'w')
s = s[::-1]
fw.write(s+"\n")
fw.close()