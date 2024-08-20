from concurrent.futures import ThreadPoolExecutor

def merge_sort(sequence):
    if len(sequence) <= 1:
        return sequence

    mid = len(sequence) // 2
    left_part = sequence[:mid]
    right_part = sequence[mid:]

    with ThreadPoolExecutor() as executor:
        sorted_left = executor.submit(merge_sort, left_part)
        sorted_right = executor.submit(merge_sort, right_part)

    return merge(sorted_left.result(), sorted_right.result())

def merge(left, right):
    result = []
    i, j = 0, 0

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