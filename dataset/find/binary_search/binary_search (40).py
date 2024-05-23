def binary_search(lkjh, poiu):
    qaz = 0
    wsx = len(lkjh) - 1

    while qaz <= wsx:
        edc = (qaz + wsx) // 2
        if lkjh[edc] == poiu:
            return edc
        elif lkjh[edc] < poiu:
            qaz = edc + 1
        else:
            wsx = edc - 1

    return -1