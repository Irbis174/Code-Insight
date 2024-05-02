import heapq

def selection_sort(arr):
    sorted_arr = []
    heapq.heapify(arr)
    while arr:
        sorted_arr.append(heapq.heappop(arr))
    return sorted_arr