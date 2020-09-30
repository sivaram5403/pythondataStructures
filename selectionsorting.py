def sort(nums):
    for i in range(len(nums)-1):
        minpos = i
        for j in range(i,6):
            if nums[j] < nums[minpos]:
                minpos = j
        temp = nums[i]
        nums[i] = nums[minpos]
        nums[minpos] = temp

        print(nums)





nums = [5,2,6,8,7,3]

sort(nums)
print(nums)