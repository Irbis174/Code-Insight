def bubble_sort(container):
    cont_len = len(container)
    swap = lambda i, j: (container[j], container[i]) if container[i] > container[j] else (container[i], container[j])
    for outer_idx in range(cont_len):
        for inner_idx in range(cont_len - outer_idx - 1):
            container[inner_idx], container[inner_idx + 1] = swap(inner_idx, inner_idx + 1)
    return container
