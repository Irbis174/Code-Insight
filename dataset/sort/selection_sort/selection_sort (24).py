import heapq

def heapq_selection_sort(lst):
    sorted_lst = []
    heapq.heapify(lst)
    while lst:
        sorted_lst.append(heapq.heappop(lst))
    return sorted_lst