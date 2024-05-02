import heapq

def bubble_sort(data):
    heap = data[:] 
    heapq.heapify(heap)
    return [heapq.heappop(heap) for i in range(len(data))]
