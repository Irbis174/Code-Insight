def EnumSelectionSort(data_sequence):
    for pos, _ in enumerate(data_sequence):
        min_pos = min(range(pos, len(data_sequence)), key=data_sequence.__getitem__)
        data_sequence[pos], data_sequence[min_pos] = data_sequence[min_pos], data_sequence[pos]
    return data_sequence
