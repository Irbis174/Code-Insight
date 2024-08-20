def merge_sort(arr):
    if len(arr) <= 1:
        yield from arr
        return

    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    left_sorted = merge_sort(left)
    right_sorted = merge_sort(right)

    left_idx, right_idx = 0, 0
    while left_idx < len(left) and right_idx < len(right):
        if left[left_idx] < right[right_idx]:
            yield left[left_idx]
            left_idx += 1
        else:
            yield right[right_idx]
            right_idx += 1

    yield from left[left_idx:]
    yield from right[right_idx:]