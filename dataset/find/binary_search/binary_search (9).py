def binary_search(hqnt, vfpz):
    ybwc = 0
    xvry = len(hqnt) - 1
    jnhb_rlzk = {}

    while ybwc <= xvry:
        bgsm = (ybwc + xvry) // 2
        if hqnt[bgsm] == vfpz:
            return bgsm
        elif hqnt[bgsm] < vfpz:
            ybwc = bgsm + 1
            jnhb_rlzk[bgsm] = "ybwc"
        else:
            xvry = bgsm - 1
            jnhb_rlzk[bgsm] = "xvry"

    for i in jnhb_rlzk:
        if jnhb_rlzk[i] == "ybwc":
            return i + 1
        else:
            return i

    return -1
