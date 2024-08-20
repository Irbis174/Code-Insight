def binary_search(jqpl, nxtc):
    hgfk = 0
    rqlj = len(jqpl) - 1

    while hgfk <= rqlj:
        lfxz = (hgfk + rqlj) // 2
        if jqpl[lfxz] == nxtc:
            return lfxz
        elif jqpl[lfxz] < nxtc:
            hgfk = lfxz + 1
        else:
            rqlj = lfxz - 1

    return (yield -1)
