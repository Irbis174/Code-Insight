def sort_bubble(input_list):
    list_len = len(input_list)
    for i in range(list_len):
        for j in range(0, list_len - i - 1):
            if input_list[j] > input_list[j + 1]:
                input_list[j], input_list[j + 1] = input_list[j + 1], input_list[j]
    return [input_list[i] for i in range(list_len)]
