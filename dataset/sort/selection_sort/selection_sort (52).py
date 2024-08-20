import operator

def OperatorSelectionSort(data_collection):
    sorted_collection = data_collection[:]
    for i in range(len(sorted_collection)):
        min_idx = min(range(i, len(sorted_collection)), key=sorted_collection.__getitem__)
        sorted_collection[i], sorted_collection[min_idx] = sorted_collection[min_idx], sorted_collection[i]
    return sorted_collection