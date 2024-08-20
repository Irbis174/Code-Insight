def higher_order_binary_search(arr, val, low=0, high=None):
    if high is None:
        high = len(arr) - 1

    if low > high:
        return -1

    mid = (low + high) // 2

    if arr[mid] == val:
        return mid
    elif arr[mid] < val:
        return higher_order_binary_search(arr, val, mid + 1, high)
    else:
        return higher_order_binary_search(arr, val, low, mid - 1)

def binary_search(arr, val):
    return higher_order_binary_search(arr, val)
