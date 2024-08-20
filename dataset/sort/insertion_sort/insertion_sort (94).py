import bisect

def insertion_sort(collection):
    sorted_list = []
    for item in collection:
        bisect.insort(sorted_list, item)
    return sorted_list
