import random

def partition(nums, left, right):
    pivot_index = random.randrange(left, right + 1)
    pivot_value = nums[pivot_index]
    nums[pivot_index], nums[right] = nums[right], nums[pivot_index]
    pivot_index = left
    for j in range(left, right):
        if nums[j] <= pivot_value:
            nums[pivot_index], nums[j] = nums[j], nums[pivot_index]
            pivot_index += 1
    nums[pivot_index], nums[right] = nums[right], nums[pivot_index]
    return pivot_index

def quicksort(nums, left_index=0, right_index=None):
    if right_index is None:
        right_index = len(nums) - 1
    if left_index < right_index:
        pivot_position = partition(nums, left_index, right_index)
        quicksort(nums, left_index, pivot_position - 1)
        quicksort(nums, pivot_position + 1, right_index)
