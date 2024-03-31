def binary_search(arr, target, comp):
    low = 0
    high = len(arr) - 1
    
    while low <= high:
        mid = (low + high) // 2
        
        if comp(arr[mid], target) == 0:
            return mid
        elif comp(arr[mid], target) < 0:
            low = mid + 1
        else:
            high = mid - 1
    
    return -1