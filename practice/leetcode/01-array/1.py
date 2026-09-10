nums = [1,2,34,56,4,5]
target = 9
n = len(nums)
for i in range(n):
    for j in range(i):
        if nums[i] + nums[j] == 9:
            print(i,j)