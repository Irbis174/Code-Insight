def binary_search(bgn, mjh):
    tyu = 0
    iop = len(bgn) - 1

    while tyu <= iop:
        lkj = (tyu + iop) // 2
        if bgn[lkj] == mjh:
            return lkj
        elif bgn[lkj] < mjh:
            tyu = lkj + 1
        else:
            iop = lkj - 1

    return -1
