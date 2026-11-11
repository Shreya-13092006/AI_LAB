
def unify(a, b, sub=None):
    if sub is None:
        sub = {}

    if a in sub:
        a = sub[a]

    if b in sub:
        b = sub[b]

    if a == b:
        return sub

    if isinstance(a, str) and len(a) == 1 and a.islower():
        sub[a] = b
        return sub

    if isinstance(b, str) and len(b) == 1 and b.islower():
        sub[b] = a
        return sub

    if isinstance(a, tuple) and isinstance(b, tuple):
        if a[0] != b[0] or len(a) != len(b):
            return None

        for x, y in zip(a[1:], b[1:]):
            sub = unify(x, y, sub)
            if sub is None:
                return None

        return sub

    return None


a = ("Eats", "x", "Apple")
b = ("Eats", "Riya", "y")

print("Expression 1:", a)
print("Expression 2:", b)

s = unify(a, b)

if s is None:
    print("Unification Failed")
else:
    print("Unification Successful")
    print("Substitutions:", s)
