import bisect

def bisect_insertion_sorter(unsorted_collection):
    sorted_list = []
    for item in unsorted_collection:
        bisect.insort(sorted_list, item)
    return sorted_list
