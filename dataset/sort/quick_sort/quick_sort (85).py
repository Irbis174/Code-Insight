def QuickSort(A):
    if len(A) <= 1:
        return A
    else:
        q = A[len(A) // 2]
        L = sorted([elem for elem in A if elem < q])
        M = [elem for elem in A if elem == q]
        R = sorted([elem for elem in A if elem > q])
        return L + M + R