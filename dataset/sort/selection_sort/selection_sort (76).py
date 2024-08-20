def selection_sort(orig_list):
    sorted_list = []
    for _ in range(len(orig_list)):
        min_val = min(orig_list)
        sorted_list.append(min_val)
        orig_list.remove(min_val)
    return sorted_list
