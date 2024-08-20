def merge_sort_impl(data):
    if len(data) > 1:
        mid = len(data) // 2
        left_part = merge_sort_impl(data[:mid])
        right_part = merge_sort_impl(data[mid:])
        return merge_impl(left_part, right_part)
    else:
        return data

def merge_impl(left, right):
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result += left[i:]
    result += right[j:]
    return result
