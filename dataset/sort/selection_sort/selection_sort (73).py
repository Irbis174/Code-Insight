def selection_sort(items):
    n = len(items)
    for i in range(n - 1):
        min_idx = i
        for j in range(i + 1, n):
            if items[j] < items[min_idx]:
                min_idx = j
        items[i], items[min_idx] = items[min_idx], items[i]
    return items
