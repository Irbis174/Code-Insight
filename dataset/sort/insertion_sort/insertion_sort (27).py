def insertion_sort_list_generator(data_list):
    for i in range(1, len(data_list)):
        curr_value = data_list[i]
        j = i
        while j > 0 and data_list[j - 1] > curr_value:
            data_list[j] = data_list[j - 1]
            j -= 1
        data_list[j] = curr_value
        yield data_list
