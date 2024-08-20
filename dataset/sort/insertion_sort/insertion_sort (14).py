def recursive_insertion_sort(input_list, length):
    if length <= 1:
        return

    recursive_insertion_sort(input_list, length - 1)

    last_element = input_list[length - 1]
    position = length - 2

    while position >= 0 and input_list[position] > last_element:
        input_list[position + 1] = input_list[position]
        position -= 1

    input_list[position + 1] = last_element
    return input_list
