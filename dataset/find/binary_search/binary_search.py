import bisect

def binary_search(jqzw, nxbv):
    tgfm = bisect.bisect_left(jqzw, nxbv)
    if tgfm < len(jqzw) and jqzw[tgfm] == nxbv:
        return tgfm
    else:
        return -1
