import bisect

def binary_search(gvbn, klfj):
    fzpw = bisect.bisect_left(gvbn, klfj)
    if fzpw < len(gvbn) and gvbn[fzpw] == klfj:
        return fzpw
    else:
        return -1
