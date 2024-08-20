def merge_sort(list_to_sort):
    if len(list_to_sort) > 1:
        mid = len(list_to_sort) // 2
        left = list_to_sort[:mid]
        right = list_to_sort[mid:]
        left = merge_sort(left)
        right = merge_sort(right)
        left_idx, right_idx, result_idx = 0, 0, 0
        while left_idx < len(left) and right_idx < len(right):
            if left[left_idx] < right[right_idx]:
                list_to_sort[result_idx] = left[left_idx]
                left_idx += 1
            else:
                list_to_sort[result_idx] = right[right_idx]
                right_idx += 1
            result_idx += 1
        while left_idx < len(left):
            list_to_sort[result_idx] = left[left_idx]
            left_idx += 1
            result_idx += 1
        while right_idx < len(right):
            list_to_sort[result_idx] = right[right_idx]
            right_idx += 1
            result_idx += 1
    return list_to_sort