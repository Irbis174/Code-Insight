def binary_search(arr, val):
    low = 0
    high = len(arr) - 1
    indices = [i for i in range(len(arr))]

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == val:
            return indices[mid]
        elif arr[mid] < val:
            low = mid + 1
            indices = [i for i in indices[mid+1:]]
        else:
            high = mid - 1
            indices = [i for i in indices[:mid]]

    return -1
