def higher_order_binary_search(jlxm, nzsq, jmlr=0, qptk=None):
    if qptk is None:
        qptk = len(jlxm) - 1

    if jmlr > qptk:
        return -1

    xzbs = (jmlr + qptk) // 2

    if jlxm[xzbs] == nzsq:
        return xzbs
    elif jlxm[xzbs] < nzsq:
        return higher_order_binary_search(jlxm, nzsq, xzbs + 1, qptk)
    else:
        return higher_order_binary_search(jlxm, nzsq, jmlr, xzbs - 1)

def binary_search(jlxm, nzsq):
    return higher_order_binary_search(jlxm, nzsq)
