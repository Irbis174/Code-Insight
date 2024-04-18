def GotoBubbleSort(array)
    length = len(array)
    start
    swapped = False
    for idx in range(1, length)
        if array[idx - 1]  array[idx]
            array[idx - 1], array[idx] = array[idx], array[idx - 1]
            swapped = True
    if swapped
        goto start
    return array
