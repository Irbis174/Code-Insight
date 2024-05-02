def generator_selection_sort(items):
    for cur_idx in range(len(items)):
        min_idx = min((j for j in range(cur_idx, len(items))), key=lambda j: items[j])
        items[cur_idx], items[min_idx] = items[min_idx], items[cur_idx]
    return items