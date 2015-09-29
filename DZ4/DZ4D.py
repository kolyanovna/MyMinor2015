__author__ = 'NikolaiEgorov'
strok = input()
nums = strok.split()
newstrok = ""
for i in range(1, len(nums)):
    if int(nums[i]) > int(nums[i-1]):
        newstrok += nums[i] + " "
print(newstrok.strip())