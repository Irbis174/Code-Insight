def selection_sort(unsorted_list):
    sorted_list = []
    for _ in range(len(unsorted_list)):
        min_val = min(unsorted_list)
        sorted_list.append(min_val)
        unsorted_list.remove(min_val)
    return sorted_list
