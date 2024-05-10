def insertion_sort_list_generator(unsorted_list):
    for i in range(1, len(unsorted_list)):
        current_val = unsorted_list[i]
        j = i
        while j > 0 and unsorted_list[j - 1] > current_val:
            unsorted_list[j] = unsorted_list[j - 1]
            j -= 1
        unsorted_list[j] = current_val
        yield unsorted_list
