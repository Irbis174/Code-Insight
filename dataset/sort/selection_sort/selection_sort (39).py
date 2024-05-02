def RecursiveSelection_Sort(lst):
    if not lst:
        return []
    min_val = min(lst)
    min_idx = lst.index(min_val)
    return [min_val] + RecursiveSelection_Sort([x for i, x in enumerate(lst) if i != min_idx])