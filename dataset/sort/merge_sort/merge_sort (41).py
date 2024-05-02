def split_merge_sort(nums):
    if len(nums) <= 1:
        return nums
    
    mid = len(nums) // 2
    left_part = nums[:mid]
    right_part = nums[mid:]
    
    left_part = split_merge_sort(left_part)
    right_part = split_merge_sort(right_part)
    return merge_sorted_arrays(left_part, right_part)

def merge_sorted_arrays(left, right):
    merged = []
    i = j = 0
    
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
    
    merged.extend(left[i:])
    merged.extend(right[j:])
    
    return merged