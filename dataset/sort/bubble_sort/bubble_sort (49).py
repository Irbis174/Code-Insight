def bubble_sort(unsorted_list):
    list_length = len(unsorted_list)
    
    def sort_slice(slice_start, slice_end):
        sliced = unsorted_list[slice_start:slice_end]
        sorted_slice = sorted(sliced, reverse=True)
        unsorted_list[slice_start:slice_end] = sorted_slice
        
    for idx in range(list_length):
        sort_slice(0, list_length - idx)
        
    return unsorted_list
