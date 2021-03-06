from math import gcd


def triplets_in_range(min, max):
    result = set([x for b in
                  range(4, max + 1, 4) for x in
                  primitive_triplets(b)])
    for x, y, z in set(result):
        a, b, c = (2 * x, 2 * y, 2 * z)
        while c <= max:
            if a >= min:
                result.add((a, b, c))
            a, b, c = (a + x, b + y, c + z)
    return set([(x, y, z) for x, y, z in result if x >= min and z <= max])


def maxMin(a, b):
    return (a, b) if a > b else (b, a)


def primitive_triplets(b):
    if b % 4 != 0:
        raise ValueError('b must be divisible by 4')
    b2 = int(b / 2)
    return set([(x[1], x[0], c) for x, c in
                [(maxMin(m2 - n2, b), m2 + n2) for m, n, m2, n2 in
                 [(m, n, int(m * m), int(n * n)) for m, n in
                  set([maxMin(m, int(b2 / m)) for m in
                       range(2, b2 + 1)
                       if b2 % m == 0])
                  if (m - n) % 2 == 1 and gcd(m, n) == 1]]])


def is_triplet(x):
    a, b, c = sorted(x)
    return a * a + b * b == c * c
