def divide_and_merge_sort(m):
    if len(m) <= 1:
        return m
    
    mid = len(m) // 2
    left_part = m[:mid]
    right_part = m[mid:]
    
    left_part = divide_and_merge_sort(left_part)
    right_part = divide_and_merge_sort(right_part)
    
    return merge_sorted_halves(left_part, right_part)

def merge_sorted_halves(left, right):
    result = []
    i = j = 0
    
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    result.extend(left[i:])
    result.extend(right[j:])
    
    return result