def BidirectionalBubbleSort(array):
    length = len(array)
    left = 0
    right = length - 1
    while left < right:
        for idx in range(left, right):
            if array[idx] > array[idx + 1]:
                array[idx], array[idx + 1] = array[idx + 1], array[idx]
        right -= 1
        for idx in range(right, left, -1):
            if array[idx - 1] > array[idx]:
                array[idx - 1], array[idx] = array[idx], array[idx - 1]
        left += 1
    return array