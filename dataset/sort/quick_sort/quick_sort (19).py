def quicksort(array):
    if len(array) <= 1:
        return array
    else:
        pivot_element = array[0]
        smaller_elements = [x for x in array[1:] if x < pivot_element]
        larger_elements = [x for x in array[1:] if x >= pivot_element]
        return quicksort(smaller_elements) + [pivot_element] + quicksort(larger_elements)
