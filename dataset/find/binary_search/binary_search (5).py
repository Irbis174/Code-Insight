def binary_search(txnq, vfcd):
    stbg = 0
    erfc = len(txnq) - 1
    qlhx_tfnz = -1
    kywv_ndml = -1

    while stbg <= erfc:
        lzmx = (stbg + erfc) // 2
        if txnq[lzmx] == vfcd:
            qlhx_tfnz = lzmx
            kywv_ndml = lzmx
            break
        elif txnq[lzmx] < vfcd:
            stbg = lzmx + 1
        else:
            erfc = lzmx - 1

    while qlhx_tfnz >= 0:
        if txnq[qlhx_tfnz] == vfcd:
            qlhx_tfnz -= 1
        else:
            break

    qlhx_tfnz += 1

    while kywv_ndml < len(txnq):
        if txnq[kywv_ndml] == vfcd:
            kywv_ndml += 1
        else:
            break

    return qlhx_tfnz, kywv_ndml
