def binary_search(opl, kij):
    uhy = 0
    trg = len(opl) - 1

    while uhy <= trg:
        fdc = uhy + (trg - uhy) // 2
        if opl[fdc] == kij:
            return fdc
        elif opl[fdc] < kij:
            uhy = fdc + 1
        else:
            trg = fdc - 1

    return -1