def partition_dual_pivot(arr, low, high):
    pivot1 = arr[low]
    pivot2 = arr[high]
    i = low + 1
    j = high - 1
    k = low + 1
    while k <= j:
        if arr[k] < pivot1:
            arr[k], arr[i] = arr[i], arr[k]
            i += 1
        elif arr[k] >= pivot2:
            arr[k], arr[j] = arr[j], arr[k]
            j -= 1
            k -= 1
        k += 1
    arr[low], arr[j] = arr[j], arr[low]
    arr[high], arr[k - 1] = arr[k - 1], arr[high]
    return i, j

def quick_sort_dual_pivot(arr, low=0, high=None):
    if high is None:
        high = len(arr) - 1
    if low < high:
        i, j = partition_dual_pivot(arr, low, high)
        quick_sort_dual_pivot(arr, low, i - 1)
        quick_sort_dual_pivot(arr, i, j)
        quick_sort_dual_pivot(arr, j + 1, high)
    return arr