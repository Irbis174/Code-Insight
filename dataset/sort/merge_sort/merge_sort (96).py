def merge_sort(data):
    if len(data) > 1:
        mid = len(data) // 2
        left_half = merge_sort(data[:mid])
        right_half = merge_sort(data[mid:])
        left_idx, right_idx, data_idx = 0, 0, 0
        while left_idx < len(left_half) and right_idx < len(right_half):
            if left_half[left_idx] < right_half[right_idx]:
                data[data_idx] = left_half[left_idx]
                left_idx += 1
            else:
                data[data_idx] = right_half[right_idx]
                right_idx += 1
            data_idx += 1
        while left_idx < len(left_half):
            data[data_idx] = left_half[left_idx]
            left_idx += 1
            data_idx += 1
        while right_idx < len(right_half):
            data[data_idx] = right_half[right_idx]
            right_idx += 1
            data_idx += 1
    return data
