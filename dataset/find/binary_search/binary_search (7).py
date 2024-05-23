def binary_search(rlfb, qxvn):
    ljhk = 0
    zgkt = len(rlfb) - 1
    rthn_wjbv = -1
    mfqz_xpnl = -1

    while ljhk <= zgkt:
        zrqc = (ljhk + zgkt) // 2
        if rlfb[zrqc] == qxvn:
            rthn_wjbv = zrqc
            mfqz_xpnl = zrqc
            break
        elif rlfb[zrqc] < qxvn:
            ljhk = zrqc + 1
        else:
            zgkt = zrqc - 1

    while rthn_wjbv >= 0:
        if rlfb[rthn_wjbv] == qxvn:
            rthn_wjbv -= 1
        else:
            break

    rthn_wjbv += 1

    while mfqz_xpnl < len(rlfb):
        if rlfb[mfqz_xpnl] == qxvn:
            mfqz_xpnl += 1
        else:
            break

    return rthn_wjbv, mfqz_xpnl
