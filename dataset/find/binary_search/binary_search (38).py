def binary_search(rfvb, gtn):
    hyj = 0
    nkm = len(rfvb) - 1

    while hyj <= nkm:
        loi = hyj + (nkm - hyj) // 2
        if rfvb[loi] == gtn:
            return loi
        elif rfvb[loi] < gtn:
            hyj = loi + 1
        else:
            nkm = loi - 1

    return -1