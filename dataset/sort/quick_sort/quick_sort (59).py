def quicksort(arr, low=0, high=None):
    if high is None:
        high = len(arr) - 1
    if low < high:
        p = partition(arr, low, high)
        quicksort(arr, low, p - 1)
        quicksort(arr, p + 1, high)
    return arr

def partition(arr, low, high):
    pivot = arr[low]
    i = low
    j = high + 1
    while True:
        while True:
            i += 1
            if arr[i] >= pivot or i == high:
                break
        while True:
            j -= 1
            if arr[j] <= pivot or j == low:
                break
        if i >= j:
            break
        arr[i], arr[j] = arr[j], arr[i]
    arr[low], arr[j] = arr[j], arr[low]
    return j