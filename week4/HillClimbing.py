import random

def h(b):
    c = 0
    for i in range(len(b)):
        for j in range(i + 1, len(b)):
            if b[i] == b[j] or abs(b[i] - b[j]) == abs(i - j):
                c += 1
    return c

def solve(n):
    while True:
        b = [random.randint(0, n - 1) for _ in range(n)]

        while True:
            cur = h(b)

            if cur == 0:
                return b

            best = b[:]
            val = cur

            for i in range(n):
                for j in range(n):
                    t = b[:]
                    t[i] = j
                    v = h(t)

                    if v < val:
                        best = t
                        val = v

            if val == cur:
                break

            b = best

n = int(input("Enter N: "))
b = solve(n)

for i in range(n):
    print(" ".join("Q" if b[j] == i else "." for j in range(n)))
