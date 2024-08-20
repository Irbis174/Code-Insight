def QuickSort(A):
    if len(A) <= 1:
        return A
    else:
        q = random.choice(A)
        L = []
        M = []
        R = []
        for elem in A:
            if elem < q:
                L.append(elem)
            elif elem > q:
                R.append(elem)
            else:
                M.append(elem)
        L.sort()
        R.sort()
        return L + M + R