def insert_sort_with_yield(list_data):
    for outer_index in range(1, len(list_data)):
        current_element = list_data[outer_index]
        inner_index = outer_index
        while inner_index > 0 and list_data[inner_index - 1] > current_element:
            list_data[inner_index] = list_data[inner_index - 1]
            inner_index -= 1
        list_data[inner_index] = current_element
        yield list_data
