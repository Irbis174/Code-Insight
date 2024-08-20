def binary_search(arr, val, low=0, high=None):
    if high is None:
        high = len(arr) - 1

    if low > high:
        return -1

    mid = (low + high) // 2

    if arr[mid] == val:
        return mid
    elif arr[mid] < val:
        return binary_search(arr, val, mid + 1, high)
    else:
        return binary_search(arr, val, low, mid - 1)
