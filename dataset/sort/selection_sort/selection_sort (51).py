import heapq

def HeapqSelectionSort(data_elements):
    sorted_elements = []
    heapq.heapify(data_elements)
    while data_elements:
        sorted_elements.append(heapq.heappop(data_elements))
    return sorted_elements