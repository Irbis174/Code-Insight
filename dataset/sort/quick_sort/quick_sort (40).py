def quicksort(unsorted_list):
    return quicksort([x for x in unsorted_list[1:] if x < unsorted_list[0]]) + \
           [unsorted_list[0]] + \
           quicksort([x for x in unsorted_list[1:] if x >= unsorted_list[0]]) if unsorted_list else []
