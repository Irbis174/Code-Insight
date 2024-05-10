import heapq

def selection_sort(arr):
    n = len(arr)
    sorted_arr = []
    heap = arr.copy()
    heapq.heapify(heap)
    for i in range(n):
        min_val = heapq.heappop(heap)
        sorted_arr.append(min_val)
    return sorted_arr
