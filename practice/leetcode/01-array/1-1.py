nums = [1,3,3,2,34,56,4,5]
target = 6
n = len(nums)
for i in range(n):
    copynums = nums.copy()
    del copynums[i]
    if ((target - nums[i]) in (copynums)):
        print(i, nums.index((target - nums[i])))