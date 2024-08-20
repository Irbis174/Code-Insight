import bisect

def binary_search(sorted_list, value):
    idx = bisect.bisect_left(sorted_list, value)
    if idx < len(sorted_list) and sorted_list[idx] == value:
        return idx
    else:
        return -1
