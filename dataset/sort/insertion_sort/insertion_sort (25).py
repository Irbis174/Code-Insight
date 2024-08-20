def list_insertion_sort(input_list):
    for idx in range(1, len(input_list)):
        current_val = input_list[idx]
        j = idx - 1
        while j >= 0 and input_list[j] > current_val:
            input_list[j + 1] = input_list[j]
            j -= 1
        input_list[j + 1] = current_val
    return input_list
