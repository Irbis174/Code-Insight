def selection_sort(nums):
    for i, _ in enumerate(nums):
        min_idx = min(range(i, len(nums)), key=nums.__getitem__)
        nums[i], nums[min_idx] = nums[min_idx], nums[i]
    return nums
