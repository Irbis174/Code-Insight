def selection_sort(values):
    for i, _ in enumerate(values):
        min_idx = min(range(i, len(values)), key=values.__getitem__)
        values[i], values[min_idx] = values[min_idx], values[i]
    return values
