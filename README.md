# Verification scripts: graceful and ρ-labelings of torus grids

Computer checks accompanying the paper

> M. F. Marashdeh, *Graceful and ρ-labelings of torus grids with an odd factor*
> (submitted to the Bulletin of the ICA).

All results of the paper are proved by hand. These scripts give an independent
check of the explicit constructions and of the finite claims.

| Script | What it checks | Paper reference |
|---|---|---|
| `verify_C4xCn.py` | Construction 3.1 is graceful for every odd n in [5, 3001]; the labeling of C4 □ C3 | Construction 3.1, Theorem 3.6, Proposition 3.8, Remark 4.9 |
| `verify_C6xCn.py` | Construction 4.1 is graceful for every odd n in [7, 1501] | Construction 4.1, Theorem 4.6, Remark 4.9 |
| `verify_small_cases.py` | The labelings of C6 □ C3, C6 □ C5 and C6 □ C7; the α-labeling of C6 □ C6 with threshold 54; the example p = 181; the 96 pairs (m, n) | Theorem 4.6, Propositions 4.7 and 4.8, Remarks 5.5 and 6.5 |

## Requirements

Python 3.8 or later. No external packages.

## Usage

```
python3 verify_C4xCn.py
python3 verify_C6xCn.py
python3 verify_small_cases.py
```

Each script prints its checks; an empty list of failures means every case passed.
Keep the three files in the same folder (`verify_small_cases.py` imports `verify_C6xCn.py`).

## Author

Mohammad F. Marashdeh, Mutah University, Karak, Jordan — marashdeh@mutah.edu.jo

## License

MIT (see `LICENSE`).
