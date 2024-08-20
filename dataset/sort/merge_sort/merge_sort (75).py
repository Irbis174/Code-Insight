def merge_sort_impl(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_part = arr[:mid]
        right_part = arr[mid:]
        left_part = merge_sort_impl(left_part)
        right_part = merge_sort_impl(right_part)
        arr = merge_impl(left_part, right_part)
    return arr

def merge_impl(left, right):
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result += left[i:]
    result += right[j:]
    return result