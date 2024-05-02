from collections import deque

def quicksort(arr):
    if not arr:
        return []
    queue = deque([(0, len(arr))])
    while queue:
        start, end = queue.popleft()
        if start >= end:
            continue
        pivot_idx = partition(arr, start, end)
        queue.append((start, pivot_idx))
        queue.append((pivot_idx + 1, end))
    return arr

def partition(arr, start, end):
    pivot = arr[end - 1]
    i = start
    for j in range(start, end - 1):
        if arr[j] < pivot:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
    arr[i], arr[end - 1] = arr[end - 1], arr[i]
    return i
