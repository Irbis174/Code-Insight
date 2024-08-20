def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_part = arr[:mid]
        right_part = arr[mid:]
        merge_sort(left_part)
        merge_sort(right_part)
        left_idx, right_idx, arr_idx = 0, 0, 0
        while left_idx < len(left_part) and right_idx < len(right_part):
            if left_part[left_idx] < right_part[right_idx]:
                arr[arr_idx] = left_part[left_idx]
                left_idx += 1
            else:
                arr[arr_idx] = right_part[right_idx]
                right_idx += 1
            arr_idx += 1
        while left_idx < len(left_part):
            arr[arr_idx] = left_part[left_idx]
            left_idx += 1
            arr_idx += 1
        while right_idx < len(right_part):
            arr[arr_idx] = right_part[right_idx]
            right_idx += 1
            arr_idx += 1
    return arr