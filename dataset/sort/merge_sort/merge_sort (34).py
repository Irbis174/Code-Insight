def merge_sort(sequence):
    if len(sequence) <= 1:
        return sequence

    left_part, right_part = split_sequence(sequence)

    sorted_left = merge_sort(left_part)
    sorted_right = merge_sort(right_part)

    return merge_sequences(sorted_left, sorted_right)

def split_sequence(sequence):
    mid = len(sequence) // 2
    left = sequence[:mid]
    right = sequence[mid:]
    return left, right

def merge_sequences(left, right):
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