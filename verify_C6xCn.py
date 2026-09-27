"""Verification of the graceful labelings of C6 x Cn, n odd.

Checks Construction 4.1 for every odd n with 7 <= n <= 1501 in
M. F. Marashdeh, "Graceful and rho-labelings of torus grids with an odd factor".
"""

# Offsets of Table 4.1: parity of k -> {row i: offset}.
LO = {1: {1: -5, 3: -7, 5: 1}, 0: {0: -4, 2: -10, 4: -12}}      # lambda_k(i)
HI = {1: {0: 13, 2: 15, 4: 7}, 0: {1: 12, 3: 2, 5: 16}}         # eta_k(i)
RLO = {1: {0: -8, 2: 0, 4: -6}, 0: {1: -13, 3: -5, 5: -11}}     # lambda'_k(i)
RHI = {1: {1: -11, 3: 3, 5: -1}, 0: {0: -10, 2: 6, 4: -6}}      # eta'_k(i)


def label6(n):
    """Labeling g of Construction 4.1 (n odd, n >= 7), as a dict (i, j) -> label."""
    E = 12 * n
    h = (n - 1) // 2
    f = {}
    for k in range(1, h):
        p = k % 2
        for i in range(6):
            f[(i, k)] = 9*k + LO[p][i] if i in LO[p] else E - 15*k + HI[p][i]
            f[(i, n - k)] = 9*k + RLO[p][i] if i in RLO[p] else E - 15*k + RHI[p][i]
    for i, v in enumerate((E - 10, E - 5, 0, E - 1, E - 4, E - 3)):
        f[(i, 0)] = v
    if n % 4 == 1:   # Table 4.2
        A, B = (-12, 0, -2, 20, 2, 22), (23, 6, 29, 57, 31, 7)
    else:
        A, B = (3, -3, 27, -5, 15, 5), (-9, 22, 0, 14, 38, 20)
    for i in range(6):
        f[(i, h)] = 9*h + A[i]
        f[(i, h + 1)] = 9*h + B[i]
    return f


def graceful(f, m, n):
    """True if f is a graceful labeling of Cm x Cn."""
    e = 2 * m * n
    vals = list(f.values())
    if len(f) != m * n or len(set(vals)) != m * n or min(vals) < 0 or max(vals) > e:
        return False
    D = sorted(abs(f[(i, j)] - f[(a, b)])
               for i in range(m) for j in range(n)
               for a, b in (((i + 1) % m, j), (i, (j + 1) % n)))
    return D == list(range(1, e + 1))


if __name__ == "__main__":
    bad = [n for n in range(7, 1502, 2) if not graceful(label6(n), 6, n)]
    print("Construction 4.1, odd n in [7, 1501]; failures:", bad)
