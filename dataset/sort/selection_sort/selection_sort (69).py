def selection_sort(elements):
    for i, _ in enumerate(elements):
        min_idx = min(range(i, len(elements)), key=elements.__getitem__)
        elements[i], elements[min_idx] = elements[min_idx], elements[i]
    return elements
