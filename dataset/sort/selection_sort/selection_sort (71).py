def selection_sort(input_list):
    sorted_list = []
    for _ in range(len(input_list)):
        min_val = min(input_list)
        sorted_list.append(min_val)
        input_list.remove(min_val)
    return sorted_list
