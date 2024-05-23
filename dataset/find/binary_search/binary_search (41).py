def binary_search(fgh, jkl):
    zxc = 0
    vbn = len(fgh) - 1

    while zxc <= vbn:
        mni = zxc + (vbn - zxc) // 2
        if fgh[mni] == jkl:
            return mni
        elif fgh[mni] < jkl:
            zxc = mni + 1
        else:
            vbn = mni - 1

    return -1