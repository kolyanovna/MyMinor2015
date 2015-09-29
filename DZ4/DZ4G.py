__author__ = 'NikolaiEgorov'
strok = input()
n1 = strok.find('h')
n2 = strok.rfind('h')
print(strok[0:n1]+strok[n2+1::])
