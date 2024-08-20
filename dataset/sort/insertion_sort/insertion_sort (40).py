def recursive_insertion_sorter(arr, n):
    if n <= 1:
        return

    recursive_insertion_sorter(arr, n - 1)

    last_elem = arr[n - 1]
    j = n - 2

    while j >= 0 and arr[j] > last_elem:
        arr[j + 1] = arr[j]
        j -= 1

    arr[j + 1] = last_elem
    return arr
