def insertion_sort_generator(lst):
    for i, x in enumerate(lst):
        j = i
        while j > 0 and lst[j - 1] > x:
            lst[j] = lst[j - 1]
            j -= 1
        lst[j] = x
        yield lst
