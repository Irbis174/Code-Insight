def merge_sort(arr):
    if not arr:
        return []

    def merge(left, right):
        result = []
        left_idx, right_idx = 0, 0

        while left_idx < len(left) and right_idx < len(right):
            if left[left_idx] < right[right_idx]:
                result.append(left[left_idx])
                left_idx += 1
            else:
                result.append(right[right_idx])
                right_idx += 1

        result.extend(left[left_idx:])
        result.extend(right[right_idx:])
        return result

    step = 1
    length = len(arr)
    temp = [None] * length

    while step < length:
        for left in range(0, length, 2 * step):
            mid = min(left + step, length)
            right = min(left + 2 * step, length)
            temp[left:right] = merge(arr[left:mid], arr[mid:right])

        step *= 2
        arr, temp = temp, arr

    return arr