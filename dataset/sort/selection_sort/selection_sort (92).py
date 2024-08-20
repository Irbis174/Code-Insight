def selection_sort(arr):
    n = len(arr)
    left = 0
    right = n - 1
    while left < right:
        min_idx = left
        max_idx = right
        for i in range(left, right + 1):
            if arr[i] < arr[min_idx]:
                min_idx = i
            elif arr[i] > arr[max_idx]:
                max_idx = i
        arr[left], arr[min_idx] = arr[min_idx], arr[left]
        if max_idx == left:
            max_idx = min_idx
        arr[right], arr[max_idx] = arr[max_idx], arr[right]
        left += 1
        right -= 
