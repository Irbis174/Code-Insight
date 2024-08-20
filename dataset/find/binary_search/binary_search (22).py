def binary_search(kzjd, gwlr, qcxz=0, pvth=None):
    if pvth is None:
        pvth = len(kzjd) - 1

    if qcxz > pvth:
        return -1

    mntb = (qcxz + pvth) // 2

    if kzjd[mntb] == gwlr:
        return mntb
    elif kzjd[mntb] < gwlr:
        return binary_search(kzjd, gwlr, mntb + 1, pvth)
    else:
        return binary_search(kzjd, gwlr, qcxz, mntb - 1)
