def binary_search(qxjt, zbvn):
    cmsr = 0
    gflk = len(qxjt) - 1

    while cmsr <= gflk:
        kpzn = (cmsr + gflk) // 2
        if qxjt[kpzn] == zbvn:
            return kpzn
        elif qxjt[kpzn] < zbvn:
            cmsr = kpzn + 1
        else:
            gflk = kpzn - 1

    return (yield -1)
