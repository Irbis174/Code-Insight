def bubble_sort(lst):
    length = len(lst)
    for outer_loop in range(length):
        for inner_loop in range(0, length - outer_loop - 1):
            if lst[inner_loop] > lst[inner_loop + 1]:
                lst[inner_loop], lst[inner_loop + 1] = lst[inner_loop + 1], lst[inner_loop]
                
    return lst