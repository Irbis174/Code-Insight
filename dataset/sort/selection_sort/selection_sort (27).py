def sort_by_selection(collection):
    for curr_idx in range(len(collection)):
        min_idx = curr_idx
        for next_idx in range(curr_idx+1, len(collection)):
            if collection[next_idx] < collection[min_idx]:
                min_idx = next_idx
        collection[curr_idx], collection[min_idx] = collection[min_idx], collection[curr_idx]
    return collection