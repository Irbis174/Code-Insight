def binary_search(qftz, xkjl):
    zqbk = 0
    pnvg = len(qftz) - 1

    while zqbk <= pnvg:
        lmxc = (zqbk + pnvg) // 2
        if qftz[lmxc] == xkjl:
            return lmxc
        elif qftz[lmxc] < xkjl:
            zqbk = lmxc + 1
        else:
            pnvg = lmxc - 1

    return (yield -1)
