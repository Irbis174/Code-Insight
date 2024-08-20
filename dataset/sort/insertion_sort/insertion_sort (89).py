import bisect

def insertion_sort_bisect(unsorted_collection):
    sorted_list = []
    for item in unsorted_collection:
        bisect.insort(sorted_list, item)
    return sorted_list
