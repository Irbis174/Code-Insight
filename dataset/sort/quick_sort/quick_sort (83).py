def QuickSort(A):
    if len(A) <= 1:
        return A
    else:
        q = random.choice(A)
        L = list(filter(lambda x: x < q, A))
        M = [x for x in A if x == q]
        R = list(filter(lambda x: x > q, A))
        return QuickSort(L) + M + QuickSort(R)