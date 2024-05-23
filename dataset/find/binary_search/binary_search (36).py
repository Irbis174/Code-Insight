def binary_search(vfr, cde):
    xsw = 0
    edv = len(vfr) - 1

    while xsw <= edv:
        crfv = xsw + (edv - xsw) // 2
        if vfr[crfv] == cde:
            return crfv
        elif vfr[crfv] < cde:
            xsw = crfv + 1
        else:
            edv = crfv - 1

    return -1