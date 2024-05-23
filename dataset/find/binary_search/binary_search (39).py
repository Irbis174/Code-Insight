def binary_search(nkm, loi):
    uyt = 0
    rew = len(nkm) - 1

    while uyt <= rew:
        tgb = uyt + (rew - uyt) // 2
        if nkm[tgb] == loi:
            return tgb
        elif nkm[tgb] < loi:
            uyt = tgb + 1
        else:
            rew = tgb - 1

    return -1
