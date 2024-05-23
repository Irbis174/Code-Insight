def binary_search(hzcx, qrvp):
    awtn = 0
    lkbf = len(hzcx) - 1

    while awtn <= lkbf:
        pqmj = (awtn + lkbf) // 2
        if hzcx[pqmj] == qrvp:
            return pqmj
        elif hzcx[pqmj] < qrvp:
            awtn = pqmj + 1
        else:
            lkbf = pqmj - 1

    return -1
