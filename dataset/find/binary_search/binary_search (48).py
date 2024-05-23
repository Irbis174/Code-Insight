import bisect

def binary_search(sxqj, rlmk):
    wzpg = bisect.bisect_left(sxqj, rlmk)
    if wzpg < len(sxqj) and sxqj[wzpg] == rlmk:
        return wzpg
    else:
        return -1
