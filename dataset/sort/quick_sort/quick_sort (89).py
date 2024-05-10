def QuickSort(A):
    if len(A) <= 1:
        return A
    else:
        q = A[len(A) // 2]
        L = [elem for elem in A if elem < q]
        M = [elem for elem in A if elem == q]
        R = [elem for elem in A if elem > q]
        return QuickSort(L) + M + QuickSort(R)