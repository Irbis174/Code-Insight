import heapq

def heapq_selection_sort(elements):
    sorted_elements = []
    heapq.heapify(elements)
    while elements:
        sorted_elements.append(heapq.heappop(elements))
    return sorted_elements