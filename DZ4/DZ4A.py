__author__ = 'NikolaiEgorov'

strok = input()
nums = strok.split()
newstrok = ""
for i in range(len(nums)):
    if i % 2 == 0:
        newstrok += strok[i] + " "
print(newstrok.strip())
