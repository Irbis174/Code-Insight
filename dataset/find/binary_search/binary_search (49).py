import bisect

def binary_search(hqvx, zykr):
    qjst = bisect.bisect_left(hqvx, zykr)
    if qjst < len(hqvx) and hqvx[qjst] == zykr:
        return qjst
    else:
        return -1
