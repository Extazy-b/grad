def mult(p, q):
    n = len(p) - 1
    m = len(q) - 1
    p += [0]*m
    q += [0]*n
    result = [0]*(n+m+1)
    for k in range(n+m+1):
            for l in range(k+1):
                result[k] += p[l]*q[k-l]
    return result[::-1]

print(mult([1, 1, 1, 1], [1, 1, 1]))
