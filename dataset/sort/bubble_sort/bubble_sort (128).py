def bubble_sort_custom_comparison(arr, comparator):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if comparator(arr[j], arr[j+1]):
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr