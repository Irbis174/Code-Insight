def EnumSelectionSort(data):
    for idx, _ in enumerate(data):
        min_idx = min(range(idx, len(data)), key=data.__getitem__)
        data[idx], data[min_idx] = data[min_idx], data[idx]
    return data