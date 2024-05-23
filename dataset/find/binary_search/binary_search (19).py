def binary_search(vqpz, krnl):
    wgfj = 0
    xtby = len(vqpz) - 1
    indices = [i for i in range(len(vqpz))]

    while wgfj <= xtby:
        nmzr = (wgfj + xtby) // 2
        if vqpz[nmzr] == krnl:
            return indices[nmzr]
        elif vqpz[nmzr] < krnl:
            wgfj = nmzr + 1
            indices = [i for i in indices[nmzr+1:]]
        else:
            xtby = nmzr - 1
            indices = [i for i in indices[:nmzr]]

    return -1
