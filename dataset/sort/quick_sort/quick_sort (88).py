from collections import deque

def QuickSort(A):
    if len(A) <= 1:
        return A
    else:
        q = random.choice(A)
        L = deque([elem for elem in A if elem < q])
        M = deque([elem for elem in A if elem == q])
        R = deque([elem for elem in A if elem > q])
        return listQuickSort(L)) + list(M) + list(QuickSort(R))