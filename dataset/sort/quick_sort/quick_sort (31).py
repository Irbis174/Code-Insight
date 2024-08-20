def partition(nums, left, right):
    pivot_value = nums[right]
    pivot_index = left - 1
    for j in range(left, right):
        if nums[j] <= pivot_value:
            pivot_index += 1
            nums[pivot_index], nums[j] = nums[j], nums[pivot_index]
    nums[pivot_index + 1], nums[right] = nums[right], nums[pivot_index + 1]
    return pivot_index + 1

def quicksort(nums, left_index=0, right_index=None):
    if right_index is None:
        right_index = len(nums) - 1
    if left_index < right_index:
        pivot_position = partition(nums, left_index, right_index)
        quicksort(nums, left_index, pivot_position - 1)
        quicksort(nums, pivot_position + 1, right_index)
