def selection_sort(container):
    n = len(container)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if container[j] < container[min_idx]:
                min_idx = j
        container[i], container[min_idx] = container[min_idx], container[i]
    return container
