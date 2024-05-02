def recursive_split_merge(nums):
    if len(nums) <= 1:
        return nums
    
    mid = len(nums) // 2
    left_part = nums[:mid]
    right_part = nums[mid:]
    
    left_part = recursive_split_merge(left_part)
    right_part = recursive_split_merge(right_part)
    
    return merge_sorted_parts(left_part, right_part)

def merge_sorted_parts(left, right):
    merged = []
    i = j = 0
    
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
    
    merged.extend(left[i:])
    merged.extend(right[j:])
    
    return merged