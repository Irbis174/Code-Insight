def introsort(arr, max_depth=None):
    if len(arr) <= 1:
        return arr
    if max_depth is None:
        max_depth = 2 * (len(arr)).bit_length()
    if max_depth == 0:
        return heapq.nlargest(len(arr), arr)
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    mid = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return introsort(left, max_depth - 1) + mid + introsort(right, max_depth - 1)