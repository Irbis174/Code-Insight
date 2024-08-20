def BubbleSort(A):
    length = len(A)
    for i in range(length):
        for j in range(0, length - i - 1):
            if A[j] > A[j + 1]:
                A[j], A[j + 1] = A[j + 1], A[j]
    A.sort()
    return A
