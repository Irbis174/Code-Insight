def partition(A, low, high):
    pivot = A[high]
    i = low
    for j in range(low, high):
        if A[j] <= pivot:
            A[i], A[j] = A[j], A[i]
            i += 1
    A[i], A[high] = A[high], A[i]
    return i

def QuickSort(A, low=0, high=None):
    if high is None:
        high = len(A) - 1
    if low < high:
        pivot_index = partition(A, low, high)
        QuickSort(A, low, pivot_index - 1)
        QuickSort(A, pivot_index + 1, high)
    return A
