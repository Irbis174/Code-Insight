def binary_search(mzkt, xbqj):
    pfvy = 0
    kbgx = len(mzkt) - 1

    while pfvy <= kbgx:
        hrwq = (pfvy + kbgx) // 2
        if mzkt[hrwq] == xbqj:
            return hrwq
        elif mzkt[hrwq] < xbqj:
            pfvy = hrwq + 1
        else:
            kbgx = hrwq - 1

    return -1
