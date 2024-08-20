def quicksort(nums):
    stack = [(0, len(nums) - 1)]
    while stack:
        left_index, right_index = stack.pop()
        if left_index >= right_index:
            continue
        pivot_value = nums[right_index]
        pivot_index = left_index - 1
        for j in range(left_index, right_index):
            if nums[j] <= pivot_value:
                pivot_index += 1
                nums[pivot_index], nums[j] = nums[j], nums[pivot_index]
        nums[pivot_index + 1], nums[right_index] = nums[right_index], nums[pivot_index + 1]
        stack.append((left_index, pivot_index - 1))
        stack.append((pivot_index + 2, right_index))
