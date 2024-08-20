def SortBySelection(data_list):
    for curr_index in range(len(data_list)):
        min_index = curr_index
        for next_index in range(curr_index+1, len(data_list)):
            if data_list[next_index] < data_list[min_index]:
                min_index = next_index
        data_list[curr_index], data_list[min_index] = data_list[min_index], data_list[curr_index]
    return data_list