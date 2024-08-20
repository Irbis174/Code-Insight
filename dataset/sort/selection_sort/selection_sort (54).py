import heapq

def selection_sort(arr):
    heap = arr.copy()
    heapq.heapify(heap)
    return [heapq.heappop(heap) for _ in range(len(arr))]
