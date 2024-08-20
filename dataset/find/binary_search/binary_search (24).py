def binary_search(vqpz, krnl, wgfj=0, xtby=None):
    if xtby is None:
        xtby = len(vqpz) - 1

    if wgfj > xtby:
        return -1

    nmzr = (wgfj + xtby) // 2

    if vqpz[nmzr] == krnl:
        return nmzr
    elif vqpz[nmzr] < krnl:
        return binary_search(vqpz, krnl, nmzr + 1, xtby)
    else:
        return binary_search(vqpz, krnl, wgfj, nmzr - 1)
