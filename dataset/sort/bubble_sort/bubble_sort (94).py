def sort_bubble(input_list, reverse=False):
    list_len = len(input_list)
    for i in range(list_len):
        swapped = False
        for j in range(0, list_len - i - 1):
            if (input_list[j] > input_list[j + 1] and not reverse) or (input_list[j] < input_list[j + 1] and reverse):
                input_list[j], input_list[j + 1] = input_list[j + 1], input_list[j]
                swapped = True
        if not swapped:
            break
    return input_list
