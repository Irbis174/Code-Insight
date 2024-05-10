def partition_random_pivot_inplace(arr, low, high):
    pivot_index = random.randint(low, high)
    arr[pivot_index], arr[high] = arr[high], arr[pivot_index]
    return partition_inplace(arr, low, high)

def quick_sort_random_pivot_inplace(arr, low=0, high=None):
    if high is None:
        high = len(arr) - 1
    if low < high:
        pivot_index = partition_random_pivot_inplace(arr, low, high)
        quick_sort_random_pivot_inplace(arr, low, pivot_index - 1)
        quick_sort_random_pivot_inplace(arr, pivot_index + 1, high)
    return arr