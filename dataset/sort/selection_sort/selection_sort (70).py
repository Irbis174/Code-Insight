def selection_sort(collection):
    n = len(collection)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if collection[j] < collection[min_idx]:
                min_idx = j
        collection[i], collection[min_idx] = collection[min_idx], collection[i]
    return collection
