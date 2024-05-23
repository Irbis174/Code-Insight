def binary_search(uyt, rew):
    tgb = 0
    vfr = len(uyt) - 1

    while tgb <= vfr:
        cde = (tgb + vfr) // 2
        if uyt[cde] < rew:
            tgb = cde + 1
        elif uyt[cde] > rew:
            vfr = cde - 1
        else:
            return cde

    return -1