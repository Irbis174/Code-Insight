from concurrent.futures import ThreadPoolExecutor

def sort_merge(sequence):
    if len(sequence) <= 1:
        return sequence

    middle = len(sequence) // 2
    left = sequence[:middle]
    right = sequence[middle:]

    with ThreadPoolExecutor() as executor:
        sorted_left = executor.submit(sort_merge, left)
        sorted_right = executor.submit(sort_merge, right)

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