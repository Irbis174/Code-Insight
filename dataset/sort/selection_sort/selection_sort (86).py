def selection_sort(original_list):
    sorted_list = []
    for _ in range(len(original_list)):
        min_val = min(original_list)
        sorted_list.append(min_val)
        original_list.remove(min_val)
    return sorted_list
