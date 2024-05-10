def merge_sort(sequence):
    if len(sequence) <= 1:
        return sequence
    mid = len(sequence) // 2
    left = merge_sort(sequence[:mid])
    right = merge_sort(sequence[mid:])
    return merge(left, right)

def merge(left, right):
    result = []
    left_idx, right_idx = 0, 0
    while left_idx < len(left) and right_idx < len(right):
        if left[left_idx] <= right[right_idx]:
            result.append(left[left_idx])
            left_idx += 1
        else:
            result.append(right[right_idx])
            right_idx += 1
    result += left[left_idx:]
    result += right[right_idx:]
    return result