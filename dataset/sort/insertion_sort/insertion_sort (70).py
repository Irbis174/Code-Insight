def insert_sort_with_yield(data):
    for i in range(1, len(data)):
        val = data[i]
        j = i
        while j > 0 and data[j - 1] > val:
            data[j] = data[j - 1]
            j -= 1
        data[j] = val
        yield data
