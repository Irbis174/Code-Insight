def merge_sort_divide(m):
    if len(m) <= 1:
        return m

    mid = len(m) // 2
    left_half = m[:mid]
    right_half = m[mid:]

    left_half = merge_sort_divide(left_half)
    right_half = merge_sort_divide(right_half)

    return merge_sorted_halves(left_half, right_half)

def merge_sorted_halves(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])

    return result