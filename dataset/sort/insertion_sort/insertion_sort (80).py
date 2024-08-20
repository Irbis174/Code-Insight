def insertion_sort_generator(data):
    for i, x in enumerate(data):
        j = i
        while j > 0 and data[j - 1] > x:
            data[j] = data[j - 1]
            j -= 1
        data[j] = x
        yield data
