import heapq

def HeapqSelectionSort(lst):
    sorted_lst = []
    heapq.heapify(lst)
    while lst:
        sorted_lst.append(heapq.heappop(lst))
    return sorted_lst
