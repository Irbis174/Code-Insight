def recursive_insertion_sort(array, n):
    if n <= 1:
        return

    recursive_insertion_sort(array, n - 1)

    last_element = array[n - 1]
    j = n - 2

    while j >= 0 and array[j] > last_element:
        array[j + 1] = array[j]
        j -= 1

    array[j + 1] = last_element
    return array
