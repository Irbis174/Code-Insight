def recursive_selection_sort(elements):
    if not elements:
        return []
    min_val = min(elements)
    min_idx = elements.index(min_val)
    return [min_val] + recursive_selection_sort([x for i, x in enumerate(elements) if i != min_idx])