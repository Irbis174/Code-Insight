def insertion_sort(lst):
    for i, value in enumerate(lst):
        j = i
        while j > 0 and lst[j - 1] > value:
            lst[j] = lst[j - 1]
            j -= 1
        lst[j] = value
        yield lst
