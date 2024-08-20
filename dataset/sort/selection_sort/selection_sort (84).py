def selection_sort(data_set):
    for i, _ in enumerate(data_set):
        min_idx = min(range(i, len(data_set)), key=data_set.__getitem__)
        data_set[i], data_set[min_idx] = data_set[min_idx], data_set[i]
    return data_set
