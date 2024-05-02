from collections import deque

def qs(arr):
    if not arr:
        return []
    q = deque([(0, len(arr))])
    while q:
        s, e = q.popleft()
        if s >= e:
            continue
        p_idx = prt(arr, s, e)
        q.append((s, p_idx))
        q.append((p_idx + 1, e))
    return arr

def prt(arr, s, e):
    p = arr[e - 1]
    i = s
    for j in range(s, e - 1):
        if arr[j] < p:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
    arr[i], arr[e - 1] = arr[e - 1], arr[i]
    return i
