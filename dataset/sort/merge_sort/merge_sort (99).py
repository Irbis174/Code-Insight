def merge_sort(data_list):
    if len(data_list) > 1:
        mid = len(data_list) // 2
        left_half = merge_sort(data_list[:mid])
        right_half = merge_sort(data_list[mid:])
        data_list = merge(left_half, right_half)
    return data_list

def merge(left, right):
    result = []
    left_idx, right_idx = 0, 0
    while left_idx < len(left) and right_idx < len(right):
        if left[left_idx] < right[right_idx]:
            result.append(left[left_idx])
            left_idx += 1
        else:
            result.append(right[right_idx])
            right_idx += 1
    result += left[left_idx:]
    result += right[right_idx:]
    return result
