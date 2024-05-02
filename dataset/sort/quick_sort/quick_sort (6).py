def quicksort(arr):
    if len(arr) <= 1:
        return arr
    smaller, equal, larger = partition(arr)
    return quicksort(smaller) + equal + quicksort(larger)

def partition(arr):
    pivot = arr[0]
    left, right = 1, len(arr) - 1
    while left <= right:
        while left <= right and arr[left] < pivot:
            left += 1
        while left <= right and arr[right] >= pivot:
            right -= 1
        if left <= right:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1
    for i in range(right + 1):
        if arr[i] >= pivot:
            arr[i], arr[right] = arr[right], arr[i]
            break
    smaller = arr[:right]
    equal = [arr[right]] * (left - right - 1)
    larger = arr[left:]
