def binary_search(znpq, kfml):
    xtrg = 0
    jbvn = len(znpq) - 1

    while xtrg <= jbvn:
        lzxc = (xtrg + jbvn) // 2
        if znpq[lzxc] == kfml:
            return lzxc
        elif znpq[lzxc] < kfml:
            xtrg = lzxc + 1
        else:
            jbvn = lzxc - 1

    return (yield -1)
