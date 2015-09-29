__author__ = 'NikolaiEgorov'

strok = input()
nums = strok.split()
newstrok = ""
for i in range(len(nums)):
    if int(nums[i]) % 2 == 0:
        newstrok += nums[i] + " "
print(newstrok.strip())