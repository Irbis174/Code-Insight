def sort_with_insertion(data_list):
    for current_index in range(1, len(data_list)):
        current_value = data_list[current_index]
        prev_index = current_index - 1
        while prev_index >= 0 and data_list[prev_index] > current_value:
            data_list[prev_index + 1] = data_list[prev_index]
            prev_index -= 1
        data_list[prev_index + 1] = current_value
    return data_list
