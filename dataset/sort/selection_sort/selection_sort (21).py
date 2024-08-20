def recursive_selection_sort(lst):
    if not lst:
        return []
    min_val = min(lst)
    min_idx = lst.index(min_val)
    return [min_val] + recursive_selection_sort([x for i, x in enumerate(lst) if i != min_idx])