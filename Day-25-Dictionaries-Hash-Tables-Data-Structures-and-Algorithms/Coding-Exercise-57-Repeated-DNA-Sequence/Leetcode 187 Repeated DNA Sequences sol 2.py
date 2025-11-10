def findRepeatedDnaSequence(s):
    L = 10
    n = len(s)
    if n <= L:
        return []

    to_int = {'A': 0, 'C': 1, 'G': 2, 'T': 3}
    nums = [to_int[c] for c in s]

    a = 4
    aL = pow(a, L)
    h = 0
    seen = set()
    output = set()

    # Compute the first hash for the first window
    for i in range(L):
        h = h * a + nums[i]
    seen.add(h)

    # Rolling hash
    for start in range(1, n - L + 1):
        h = h * a - nums[start - 1] * aL + nums[start + L - 1]

        if h in seen:
            output.add(s[start:start + L])
        else:
            seen.add(h)

    return list(output)


print(findRepeatedDnaSequence("GAAAATCCCCGAAAATCCCCGAAAAAGGGTTT"))
