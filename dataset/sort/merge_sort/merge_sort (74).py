def merge_sort_impl(sequence):
    if len(sequence) <= 1:
        return sequence
    mid = len(sequence) // 2
    left = merge_sort_impl(sequence[:mid])
    right = merge_sort_impl(sequence[mid:])
    return merge_impl(left, right)

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