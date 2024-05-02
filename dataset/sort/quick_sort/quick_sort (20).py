def quicksort(array):
    return quicksort([x for x in array[1:] if x < array[0]]) + \
           [array[0]] + \
           quicksort([x for x in array[1:] if x >= array[0]]) if array else []
