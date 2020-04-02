def combination(n, k):
    if k == 0:
        return [[0] * n]
    if n == k:
        return [[1] * n]
    res1 = combination(n - 1, k - 1)
    for res in res1:
        res.insert(0, 1)
    res0 = combination(n - 1, k)
    for res in res0:
        res.insert(0, 0)
    res1.extend(res0)
    return res1

# print(len(combination(50, 4)))
