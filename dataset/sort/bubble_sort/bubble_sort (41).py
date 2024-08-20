def bubble_sort(collection):
    coll_len = len(collection)
    for outer_idx in range(coll_len):
        for inner_idx in range(0, coll_len - outer_idx - 1):
            if collection[inner_idx] > collection[inner_idx + 1]:
                temp_val = collection[inner_idx]
                collection[inner_idx] = collection[inner_idx + 1]
                collection[inner_idx + 1] = temp_val
    return collection
