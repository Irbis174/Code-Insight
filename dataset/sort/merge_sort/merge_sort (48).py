def merge_sort(lst):
    def merge(left, right):
        result = []
        i, j = 0, 0

        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1

        result.extend(left[i:])
        result.extend(right[j:])

        return result

    if len(lst) <= 1:
        return lst

    stack = [(0, len(lst))]
    result = []

    while stack:
        start, end = stack.pop()
        if end - start <= 1:
            continue

        mid = (start + end) // 2
        stack.extend([(start, mid), (mid, end)])
        result.append((start, mid, end))

    for start, mid, end in reversed(result):
        lst[start:end] = merge(lst[start:mid], lst[mid:end])

    return lst
