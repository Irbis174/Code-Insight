def higher_order_binary_search(klnm, zyvx, qgtr=0, bfht=None):
    if bfht is None:
        bfht = len(klnm) - 1

    if qgtr > bfht:
        return -1

    nvwc = (qgtr + bfht) // 2

    if klnm[nvwc] == zyvx:
        return nvwc
    elif klnm[nvwc] < zyvx:
        return higher_order_binary_search(klnm, zyvx, nvwc + 1, bfht)
    else:
        return higher_order_binary_search(klnm, zyvx, qgtr, nvwc - 1)

def binary_search(klnm, zyvx):
    return higher_order_binary_search(klnm, zyvx)

