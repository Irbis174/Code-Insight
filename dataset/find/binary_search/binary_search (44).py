def binary_search(xsw, edv):
    crf = 0
    vgb = len(xsw) - 1

    while crf <= vgb:
        hnj = (crf + vgb) // 2
        if xsw[hnj] == edv:
            return hnj
        elif xsw[hnj] < edv:
            crf = hnj + 1
        else:
            vgb = hnj - 1

    return -1