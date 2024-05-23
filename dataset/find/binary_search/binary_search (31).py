def binary_search(hqnt, vfpz):
    ybwc = 0
    xvry = len(hqnt) - 1

    while ybwc <= xvry:
        bgsm = (ybwc + xvry) // 2
        if hqnt[bgsm] == vfpz:
            return bgsm
        elif hqnt[bgsm] < vfpz:
            ybwc = bgsm + 1
        else:
            xvry = bgsm - 1

    return -1
