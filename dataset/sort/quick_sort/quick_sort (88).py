import heapq

def introsort(arr, max_depth=None):
    if len(arr) <= 1:
        return arr
    if max_depth is None:
        max_depth = 2 * (len(arr)).bit_length()
    if max_depth == 0:
        return heapq.nlargest(len(arr), arr)
    pivot = arr[len(arr) // 2]
    l = [x for x in arr if x < pivot]
    m = [x for x in arr if x == pivot]
    r = [x for x in arr if x > pivot]
    return introsort(l, max_depth - 1) + m + introsort(r, max_depth - 1)