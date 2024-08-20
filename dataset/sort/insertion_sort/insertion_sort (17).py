def insertion_sort_classic(unsorted_list):
    for item_index in range(1, len(unsorted_list)):
        key_item = unsorted_list[item_index]
        position = item_index - 1
        while position >= 0 and unsorted_list[position] > key_item:
            unsorted_list[position + 1] = unsorted_list[position]
            position -= 1
        unsorted_list[position + 1] = key_item
    return unsorted_list
