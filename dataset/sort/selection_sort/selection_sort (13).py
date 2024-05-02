def selection_sort(nums):
    sorted_nums = []
    for _ in range(len(nums)):
        min_val = min(nums)
        sorted_nums.append(min_val)
        nums.remove(min_val)
    return sorted_nums
