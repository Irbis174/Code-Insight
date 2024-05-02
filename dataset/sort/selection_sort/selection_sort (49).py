def ComprehensionSelectionSort(data_values):
    sorted_values = []
    for _ in range(len(data_values)):
        min_val = min(data_values)
        sorted_values.append(min_val)
        data_values.remove(min_val)
    return sorted_values