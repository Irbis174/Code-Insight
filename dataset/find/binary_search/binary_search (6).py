def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    if arr[low] > target or arr[high] < target:
        return -1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1