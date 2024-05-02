def bubble_sort(data):
    data_len = len(data)
    swapped = True
    while swapped:
        swapped = False
        for idx in range(data_len - 1):
            if data[idx] > data[idx + 1]:
                data[idx], data[idx + 1] = data[idx + 1], data[idx]
                swapped = True
    return data
