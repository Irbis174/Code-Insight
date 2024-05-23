def binary_search(jlxm, nzsq):
    jmlr = 0
    qptk = len(jlxm) - 1
    indices = [i for i in range(len(jlxm))]

    while jmlr <= qptk:
        xzbs = (jmlr + qptk) // 2
        if jlxm[xzbs] == nzsq:
            return indices[xzbs]
        elif jlxm[xzbs] < nzsq:
            jmlr = xzbs + 1
            indices = [i for i in indices[xzbs+1:]]
        else:
            qptk = xzbs - 1
            indices = [i for i in indices[:xzbs]]

    return -1
