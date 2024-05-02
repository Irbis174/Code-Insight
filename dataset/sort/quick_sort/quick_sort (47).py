def quicksort(unsorted_list):
    if len(unsorted_list) <= 1:
        return unsorted_list
    else:
        pivot_value = unsorted_list[0]
        left_sublist = [x for x in unsorted_list[1:] if x < pivot_value]
        right_sublist = [x for x in unsorted_list[1:] if x >= pivot_value]
        left_sublist = quicksort(left_sublist)
        right_sublist = quicksort(right_sublist)
        return left_sublist + [pivot_value] + right_sublist
