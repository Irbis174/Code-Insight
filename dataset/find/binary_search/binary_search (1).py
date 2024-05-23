def binary_search(arr, target):
    left = 0
    right = len(arr) - 1
    lower_bound = -1
    upper_bound = -1

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            lower_bound = mid
            upper_bound = mid
            break
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    while lower_bound >= 0:
        if arr[lower_bound] == target:
            lower_bound -= 1
        else:
            break

    lower_bound += 1

    while upper_bound < len(arr):
        if arr[upper_bound] == target:
            upper_bound += 1
        else:
            break

    return lower_bound, upper_bound
