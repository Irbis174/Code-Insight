def binary_search(lst, target):
    left = 0
    right = len(lst) - 1
    index_map = {}

    while left <= right:
        mid = (left + right) // 2
        if lst[mid] == target:
            return mid
        elif lst[mid] < target:
            left = mid + 1
            index_map[mid] = "left"
        else:
            right = mid - 1
            index_map[mid] = "right"

    for i in index_map:
        if index_map[i] == "left":
            return i + 1
        else:
            return i

    return -1
