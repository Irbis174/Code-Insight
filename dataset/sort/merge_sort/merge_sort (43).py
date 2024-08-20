def sort_merge(mas):
    if len(mas) <= 1:
        return mas
    
    mid = len(mas) // 2
    left_part = mas[:mid]
    right_part = mas[mid:]
    
    left_part = sort_merge(left_part)
    right_part = sort_merge(right_part)
    
    return merge_sorted(left_part, right_part)

def merge_sorted(left, right):
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