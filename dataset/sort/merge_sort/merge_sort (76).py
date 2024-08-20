def merge_sort_impl(data):
    if len(data) > 1:
        mid = len(data) // 2
        left_half = merge_sort_impl(data[:mid])
        right_half = merge_sort_impl(data[mid:])
        i, j, k = 0, 0, 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                data[k] = left_half[i]
                i += 1
            else:
                data[k] = right_half[j]
                j += 1
            k += 1
        while i < len(left_half):
            data[k] = left_half[i]
            i += 1
            k += 1
        while j < len(right_half):
            data[k] = right_half[j]
            j += 1
            k += 1
    return data