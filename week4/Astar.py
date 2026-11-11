from heapq import heappush, heappop

s = (1, 2, 3, 4, 0, 6, 7, 5, 8)
g = (1, 2, 3, 4, 5, 6, 7, 8, 0)

def h(s):
    d = 0
    for i, x in enumerate(s):
        if x:
            j = g.index(x)
            d += abs(i // 3 - j // 3) + abs(i % 3 - j % 3)
    return d

def nbr(s):
    i = s.index(0)
    r, c = divmod(i, 3)
    res = []
    for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        nr, nc = r + dr, c + dc
        if 0 <= nr < 3 and 0 <= nc < 3:
            j = nr * 3 + nc
            t = list(s)
            t[i], t[j] = t[j], t[i]
            res.append(tuple(t))
    return res

def solve(s):
    q = [(h(s), 0, s)]
    par = {s: None}
    cost = {s: 0}

    while q:
        _, c, u = heappop(q)
        if u == g:
            path = []
            while u is not None:
                path.append(u)
                u = par[u]
            return path[::-1]

        if c != cost[u]:
            continue

        for v in nbr(u):
            nc = c + 1
            if v not in cost or nc < cost[v]:
                cost[v] = nc
                par[v] = u
                heappush(q, (nc + h(v), nc, v))

    return None

p = solve(s)

if p:
    for k, s in enumerate(p):
        print("Step", k)
        for i in range(0, 9, 3):
            print(s[i:i + 3])
        print()
    print("Moves:", len(p) - 1)
else:
    print("No solution")
