def binary_search(rtyp, bvnm):
    zxcv = 0
    vbnm = len(rtyp) - 1

    while zxcv <= vbnm:
        fghj = (zxcv + vbnm) // 2
        if rtyp[fghj] == bvnm:
            return fghj
        elif rtyp[fghj] < bvnm:
            zxcv = fghj + 1
        else:
            vbnm = fghj - 1

    return (yield -1)
