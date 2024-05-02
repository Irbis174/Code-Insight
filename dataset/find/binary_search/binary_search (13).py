def binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    
    while low <= high:
        mid = (low + high) // 2

        if arr[mid][0] == target:
            return arr[mid][1]
        elif arr[mid][0] < target:
            low = mid + 1
        else:
            high = mid - 1
    
    return -1