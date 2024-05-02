def qs(arr):
    if len(arr) <= 1:
        return arr
    s, e, l = prt(arr)
    return qs(s) + e + qs(l)

def prt(arr):
    p = arr[0]
    a, b = 1, len(arr) - 1
    while a <= b:
        while a <= b and arr[a] < p:
            a += 1
        while a <= b and arr[b] >= p:
            b -= 1
        if a <= b:
            arr[a], arr[b] = arr[b], arr[a]
            a += 1
            b -= 1
    for i in range(b + 1):
        if arr[i] >= p:
            arr[i], arr[b] = arr[b], arr[i]
            break
    s = arr[:b]
    e = [arr[b]] * (a - b - 1)
    l = arr[a:]
    return s, e, l
