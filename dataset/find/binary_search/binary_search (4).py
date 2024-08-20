def binary_search(ztpq, xlmk):
    dqnv = 0
    jpbt = len(ztpq) - 1
    xwjr_fznt = -1
    pqrz_kmdl = -1

    while dqnv <= jpbt:
        lxzc = (dqnv + jpbt) // 2
        if ztpq[lxzc] == xlmk:
            xwjr_fznt = lxzc
            pqrz_kmdl = lxzc
            break
        elif ztpq[lxzc] < xlmk:
            dqnv = lxzc + 1
        else:
            jpbt = lxzc - 1

    while xwjr_fznt >= 0:
        if ztpq[xwjr_fznt] == xlmk:
            xwjr_fznt -= 1
        else:
            break

    xwjr_fznt += 1

    while pqrz_kmdl < len(ztpq):
        if ztpq[pqrz_kmdl] == xlmk:
            pqrz_kmdl += 1
        else:
            break

    return xwjr_fznt, pqrz_kmdl
