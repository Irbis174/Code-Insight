def insertion_sort_recursive(data, n):
    if n <= 1:
        return

    insertion_sort_recursive(data, n - 1)

    last_elem = data[n - 1]
    j = n - 2

    while j >= 0 and data[j] > last_elem:
        data[j + 1] = data[j]
        j -= 1

    data[j + 1] = last_elem
    return data
