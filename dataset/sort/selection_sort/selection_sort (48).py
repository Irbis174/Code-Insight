def RecursiveSelection_Sort(data_elements):
    if not data_elements:
        return []
    min_val = min(data_elements)
    min_idx = data_elements.index(min_val)
    return [min_val] + RecursiveSelection_Sort([x for i, x in enumerate(data_elements) if i != min_idx])