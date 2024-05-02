import operator

def operator_selection_sort(data):
    sorted_data = data[:]
    for i in range(len(sorted_data)):
        min_idx = min(range(i, len(sorted_data)), key=sorted_data.__getitem__)
        sorted_data[i], sorted_data[min_idx] = sorted_data[min_idx], sorted_data[i]
    return sorted_data