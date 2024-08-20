import bisect

def insertion_sort(lst):
    sorted_lst = []
    for val in lst:
        bisect.insort(sorted_lst, val)
    return sorted_lst
