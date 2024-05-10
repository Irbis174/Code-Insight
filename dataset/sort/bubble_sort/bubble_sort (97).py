def sort_bubble(input_list):
    list_len = len(input_list)
    for i in range(list_len):
        swapped = False
        for j in range(0, list_len - i - 1):
            if str(input_list[j]) > str(input_list[j + 1]):
                input_list[j], input_list[j + 1] = input_list[j + 1], input_list[j]
                swapped = True
        if not swapped:
            break
    return input_list
