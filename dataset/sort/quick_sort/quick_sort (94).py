def partition_three_way(arr, low, high):
    pivot = arr[low]
    i = low
    j = high
    for k in range(low, high):
        if arr[k] < pivot:
            arr[k], arr[i] = arr[i], arr[k]
            i += 1
        elif arr[k] > pivot:
            arr[k], arr[j] = arr[j], arr[k]
            j -= 1
            k -= 1
    return i, j

def quick_sort_three_way(arr, low=0, high=None):
    if high is None:
        high = len(arr) - 1
    if low < high:
        i, j = partition_three_way(arr, low, high)
        quick_sort_three_way(arr, low, i - 1)
        quick_sort_three_way(arr, j + 1, high)
    return arr