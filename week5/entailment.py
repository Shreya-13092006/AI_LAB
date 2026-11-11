
from itertools import product

print("P Q R | Q->P P->~Q Q|R | KB")

mods = []

for p, q, r in product([False, True], repeat=3):
    a = not q or p
    b = not p or not q
    c = q or r
    kb = a and b and c

    print(int(p), int(q), int(r), "|", int(a), int(b), int(c), "|", int(kb))

    if kb:
        mods.append((p, q, r))

print("\nKB Models:", mods)

queries = {
    "R": lambda p, q, r: r,
    "R -> P": lambda p, q, r: not r or p,
    "Q -> R": lambda p, q, r: not q or r
}

for name, fn in queries.items():
    ans = all(fn(*m) for m in mods)
    print(name, ":", "Entails" if ans else "Does not entail")
