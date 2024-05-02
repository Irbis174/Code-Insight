def bubble_sort(unsorted_data):
    data_len = len(unsorted_data)
    swapped = True

    while swapped:
        swapped = False
        unsorted_data = list(map(lambda i, j: (j, i) if unsorted_data[i] > unsorted_data[j] else (i, j),
                                 unsorted_data[:-1], unsorted_data[1:]))
        swapped = any(unsorted_data[i] > unsorted_data[i+1] for i in range(data_len-1))
        unsorted_data = [unsorted_data[j] for i, j in enumerate(map(lambda i, j: (i, j) if i < j else (j, i),
                                                                    range(data_len), unsorted_data))]

    return unsorted_data
