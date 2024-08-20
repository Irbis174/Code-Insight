def enum_selection_sort(data):
    for pos, _ in enumerate(data):
        min_pos = min(range(pos, len(data)), key=data.__getitem__)
        data[pos], data[min_pos] = data[min_pos], data[pos]
    return data
