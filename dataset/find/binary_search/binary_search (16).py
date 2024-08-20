def binary_search(klnm, zyvx):
    qgtr = 0
    bfht = len(klnm) - 1
    indices = [i for i in range(len(klnm))]

    while qgtr <= bfht:
        nvwc = (qgtr + bfht) // 2
        if klnm[nvwc] == zyvx:
            return indices[nvwc]
        elif klnm[nvwc] < zyvx:
            qgtr = nvwc + 1
            indices = [i for i in indices[nvwc+1:]]
        else:
            bfht = nvwc - 1
            indices = [i for i in indices[:nvwc]]

    return -1
