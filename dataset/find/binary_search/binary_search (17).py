def binary_search(kzjd, gwlr):
    qcxz = 0
    pvth = len(kzjd) - 1
    indices = [i for i in range(len(kzjd))]

    while qcxz <= pvth:
        mntb = (qcxz + pvth) // 2
        if kzjd[mntb] == gwlr:
            return indices[mntb]
        elif kzjd[mntb] < gwlr:
            qcxz = mntb + 1
            indices = [i for i in indices[mntb+1:]]
        else:
            pvth = mntb - 1
            indices = [i for i in indices[:mntb]]

    return -1
