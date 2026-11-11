
import random
import math

def h(a):
    c = 0
    for i in range(8):
        for j in range(i + 1, 8):
            if a[i] == a[j] or abs(a[i] - a[j]) == j - i:
                c += 1
    return c

a = [random.randint(0, 7) for i in range(8)]
t = 100

while t > 0.1:
    if h(a) == 0:
        break

    b = a[:]
    i = random.randint(0, 7)
    b[i] = random.randint(0, 7)

    d = h(b) - h(a)

    if d < 0 or random.random() < math.exp(-d / t):
        a = b

    t *= 0.99

print("Board:")
for i in range(8):
    print(["Q" if a[j] == i else "." for j in range(8)])

if h(a) == 0:
    print("Solution Found")
else:
    print("Solution Not Found")
