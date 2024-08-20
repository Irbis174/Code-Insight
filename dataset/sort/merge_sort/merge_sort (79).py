def merge_sort_impl(data_list):
    if len(data_list) > 1:
        mid = len(data_list) // 2
        left_half = merge_sort_impl(data_list[:mid])
        right_half = merge_sort_impl(data_list[mid:])
        data_list = merge_impl(left_half, right_half)
    return data_list

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