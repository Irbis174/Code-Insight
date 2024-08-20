def selection_sort(L):
    sorted_L = []
    for _ in range(len(L)):
        min_val = min(L)
        sorted_L.append(min_val)
        L.remove(min_val)
    return sorted_L
