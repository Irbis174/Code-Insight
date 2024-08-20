def sort_merge(sequence):
    if len(sequence) <= 1:
        return sequence

    left, right = split_list(sequence)

    sorted_left = sort_merge(left)
    sorted_right = sort_merge(right)

    return merge_lists(sorted_left, sorted_right)

def split_list(sequence):
    middle = len(sequence) // 2
    left = sequence[:middle]
    right = sequence[middle:]
    return left, right

def merge_lists(left, right):
    merged = []
    i, j = 0, 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1

    merged.extend(left[i:])
    merged.extend(right[j:])

    return merged