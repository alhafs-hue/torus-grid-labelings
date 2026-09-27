"""Verification of the graceful labelings of C4 x Cn, n odd.

Checks Construction 3.1 for every odd n with 5 <= n <= 3001, and the labeling
of Proposition 3.8 for n = 3, in
M. F. Marashdeh, "Graceful and rho-labelings of torus grids with an odd factor".
"""


def label(n):
    """Labeling f of Construction 3.1 (n odd, n >= 5), as a dict (i, j) -> label."""
    E = 8 * n
    h = (n - 1) // 2
    f = {}
    eps = lambda i: 1 if i >= 2 else 0
    for i, v in enumerate((E - 4, E - 1, 0, 1)):
        f[(i, 0)] = v
    for k in range(1, h):
        for i in range(4):
            f[(i, k)] = 6*k - 4 + 4*eps(i) if (i + k) % 2 == 0 else E - 10*k + 8 + 2*eps(i)
            f[(i, n - k)] = 6*k - 1 + 4*eps(i) if (i + k) % 2 == 1 else E - 10*k + 2 + 2*eps(i)
    if n % 4 == 1:
        gh, gh1 = (-7, 15, -1, 12), (1, -3, 9, -5)
    else:
        gh, gh1 = (-17, 9, 15, 5), (1, 20, 7, 22)
    for i in range(4):
        f[(i, h)] = 3*n + gh[i]
        f[(i, h + 1)] = 3*n + gh1[i]
    return f


def label3():
    """Labeling of C4 x C3 in Proposition 3.8."""
    rows = [[0, 2, 24], [1, 22, 5], [14, 4, 20], [23, 9, 12]]
    return {(i, j): rows[i][j] for i in range(4) for j in range(3)}


def is_graceful(f, m, n):
    """True if f is a graceful labeling of Cm x Cn."""
    e = 2 * m * n
    vals = list(f.values())
    if len(f) != m * n or len(set(vals)) != m * n or min(vals) < 0 or max(vals) > e:
        return False
    D = [abs(f[(i, j)] - f[(a, b)])
         for i in range(m) for j in range(n)
         for a, b in (((i + 1) % m, j), (i, (j + 1) % n))]
    return sorted(D) == list(range(1, e + 1))


if __name__ == "__main__":
    print("n = 3 (Proposition 3.8):", "graceful" if is_graceful(label3(), 4, 3) else "FAIL")
    bad = [n for n in range(5, 3002, 2) if not is_graceful(label(n), 4, n)]
    print("Construction 3.1, odd n in [5, 3001]; failures:", bad)
