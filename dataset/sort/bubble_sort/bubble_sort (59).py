def BubbleSort(A):
    length = len(A)
    for i in range(length):
        is_swapped = False
        for j in range(0, length - i - 1):
            if A[j] > A[j + 1]:
                A[j], A[j + 1] = A[j + 1], A[j]
                is_swapped = True
        if not is_swapped:
            break
    if length > 1:
        return BubbleSort([A[i] for i in range(1, length)])
    else:
        return A
