def binary_search(mfqz, xrvb):
    zhsx = 0
    tbfg = len(mfqz) - 1
    khrj_tmsj = -1
    rcgl_dvzw = -1

    while zhsx <= tbfg:
        jnxq = (zhsx + tbfg) // 2
        if mfqz[jnxq] == xrvb:
            khrj_tmsj = jnxq
            rcgl_dvzw = jnxq
            break
        elif mfqz[jnxq] < xrvb:
            zhsx = jnxq + 1
        else:
            tbfg = jnxq - 1

    while khrj_tmsj >= 0:
        if mfqz[khrj_tmsj] == xrvb:
            khrj_tmsj -= 1
        else:
            break

    khrj_tmsj += 1

    while rcgl_dvzw < len(mfqz):
        if mfqz[rcgl_dvzw] == xrvb:
            rcgl_dvzw += 1
        else:
            break

    return khrj_tmsj, rcgl_dvzw
