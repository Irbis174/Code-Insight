def binary_search(zqpx, lmfk):
    trgv = 0
    bznj = len(zqpx) - 1
    xqjr_ztcl = {}

    while trgv <= bznj:
        nvbz = (trgv + bznj) // 2
        if zqpx[nvbz] == lmfk:
            return nvbz
        elif zqpx[nvbz] < lmfk:
            trgv = nvbz + 1
            xqjr_ztcl[nvbz] = "trgv"
        else:
            bznj = nvbz - 1
            xqjr_ztcl[nvbz] = "bznj"

    for i in xqjr_ztcl:
        if xqjr_ztcl[i] == "trgv":
            return i + 1
        else:
            return i

    return -1
