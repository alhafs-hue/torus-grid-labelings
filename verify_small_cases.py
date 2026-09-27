# Verification of the finite claims in Marashdeh, "Graceful and rho-labelings of
# torus grids with an odd factor": Propositions 3.8, 4.7, 4.8, the n = 7 matrix
# in Theorem 4.6, Remark 5.5 (p = 181) and Remark 6.5 (the 96 pairs).
from math import gcd

def diffs(L):
    m, n = len(L), len(L[0])
    return ([abs(L[i][j] - L[(i+1) % m][j]) for i in range(m) for j in range(n)] +
            [abs(L[i][j] - L[i][(j+1) % n]) for i in range(m) for j in range(n)])

def graceful(L):
    e = 2 * len(L) * len(L[0]); labs = [x for r in L for x in r]
    return (len(set(labs)) == len(labs) and 0 <= min(labs) and max(labs) <= e
            and sorted(diffs(L)) == list(range(1, e + 1)))

P38 = [[0,2,24],[1,22,5],[14,4,20],[23,9,12]]
P47a = [[0,1,36],[2,35,9],[34,4,24],[12,20,33],[31,26,8],[3,15,32]]
P47b = [[0,1,17,39,60],[23,25,37,29,20],[27,10,43,16,45],[53,42,8,44,14],[12,5,51,6,56],[59,54,3,58,2]]
N7 = [[74,82,14,30,18,44,1],[79,4,66,24,49,5,58],[0,84,8,54,27,60,9],
      [83,2,56,22,41,13,72],[80,76,6,42,65,48,3],[81,10,70,32,47,7,68]]
P48 = [[54,55,53,68,3,61],[71,1,56,5,72,0],[49,63,52,64,4,57],
       [69,31,62,22,70,51],[13,65,21,58,37,60],[59,16,66,42,67,32]]
print("Proposition 3.8 (C4 x C3):", graceful(P38))
print("Proposition 4.7 (C6 x C3, C6 x C5):", graceful(P47a), graceful(P47b))
print("Theorem 4.6, n = 7 matrix:", graceful(N7))
alpha = graceful(P48) and all((P48[i][j] <= 54) == ((i + j) % 2 == 0) for i in range(6) for j in range(6))
print("Proposition 4.8 (C6 x C6) alpha-labeling, threshold 54:", alpha)
try:
    from verify_C6xCn import label6
    g = label6(7)
    print("n = 7 matrix equals Construction 4.1:", all(g[(i, j)] == N7[i][j] for i in range(6) for j in range(7)))
except Exception as exc:
    print("(comparison with Construction 4.1 skipped:", exc, ")")

def is_prime(q):
    return q > 1 and all(q % d for d in range(2, int(q**0.5) + 1))

def elements_of_order(k, p):
    return [x for x in range(2, p) if pow(x, k, p) == 1 and all(pow(x, k // q, p) != 1 for q in range(2, k + 1) if k % q == 0 and is_prime(q))]

def nonsquare(x, p):
    return pow(x % p, (p - 1) // 2, p) == p - 1

# Remark 5.5: (m,n,p) = (3,5,181), t = 3, s = 1: (alpha-1)/(beta-1) is always a square.
p = 181
A, B = elements_of_order(3, p), elements_of_order(5, p)
print("Remark 5.5: order-3", A, "order-5", B,
      "; all ratios squares:", all(not nonsquare((a - 1) * pow(b - 1, -1, p), p) for a in A for b in B))

# Remark 6.5: coprime odd 3 <= m < n, m < 40, n < 60, 4mn+1 prime.
pairs = [(m, n) for m in range(3, 40, 2) for n in range(m + 2, 60, 2) if gcd(m, n) == 1 and is_prime(4*m*n + 1)]
ok = [(m, n) for m, n in pairs
      if any(nonsquare((a - 1) * (b - 1), 4*m*n + 1) for a in elements_of_order(m, 4*m*n + 1) for b in elements_of_order(n, 4*m*n + 1))]
print("Remark 6.5: pairs =", len(pairs), "; condition holds for", len(ok))
