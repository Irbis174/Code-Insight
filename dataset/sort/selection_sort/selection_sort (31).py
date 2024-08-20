def comprehension_selection_sort(values):
    sorted_values = []
    for _ in range(len(values)):
        min_val = min(values)
        sorted_values.append(min_val)
        values.remove(min_val)
    return sorted_values