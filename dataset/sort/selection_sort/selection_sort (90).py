def selection_sort(unsorted_data):
    sorted_data = []
    for _ in range(len(unsorted_data)):
        min_val = min(unsorted_data)
        sorted_data.append(min_val)
        unsorted_data.remove(min_val)
    return sorted_data
