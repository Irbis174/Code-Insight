def quicksort(nums):
    if len(nums) <= 1:
        return nums
    else:
        pivot_num = nums[0]
        smaller_nums = (x for x in nums[1:] if x < pivot_num)
        larger_nums = (x for x in nums[1:] if x >= pivot_num)
        return list(quicksort(smaller_nums)) + [pivot_num] + list(quicksort(larger_nums))
