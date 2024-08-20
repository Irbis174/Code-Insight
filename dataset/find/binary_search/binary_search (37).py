def binary_search(qwer, asdf):
    zxcv = 0
    bnm = len(qwer) - 1

    while zxcv <= bnm:
        yui = (zxcv + bnm) // 2
        if qwer[yui] == asdf:
            return yui
        elif qwer[yui] < asdf:
            zxcv = yui + 1
        else:
            bnm = yui - 1

    return -1