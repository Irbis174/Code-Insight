def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_part = arr[:mid]
        right_part = arr[mid:]
        left_part = merge_sort(left_part)
        right_part = merge_sort(right_part)
        arr = merge(left_part, right_part)
    return arr

def merge(left, right):
    result = []
    left_idx, right_idx = 0, 0
    while left_idx < len(left) and right_idx < len(right):
        if left[left_idx] <= right[right_idx]:
            result.append(left[left_idx])
            left_idx += 1
        else:
            result.append(right[right_idx])
            right_idx += 1
    result += left[left_idx:]
    result += right[right_idx:]
    return result