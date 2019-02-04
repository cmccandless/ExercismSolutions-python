from functools import partial
from itertools import chain, cycle
try:
    from math import gcd
except ImportError:
    from fractions import gcd

ALPHA_START = ord('a')
ALPHA_LENGTH = ord('z') - ALPHA_START + 1


def mmi(a, m=ALPHA_LENGTH):
    n = 1
    while (n * a) % m != 1:
        n += 1
    return n


def with_spaces(every_n_chars):
    def insert_spaces_at(n_chars, s):
        return ''.join(chain(*zip(
            s,
            cycle(
                [''] * (n_chars - 1) + [' ']
                if n_chars > 0 else
                ['']
            )
        ))).rstrip()
    return partial(insert_spaces_at, every_n_chars)


def transcode(with_spaces, transform, text, a, b):
    if gcd(a, ALPHA_LENGTH) != 1:
        raise ValueError('a and m must be coprime')
    return with_spaces(
        chr(
            transform(
                ord(c) - ALPHA_START, a, b
            ) % ALPHA_LENGTH + ALPHA_START
        )
        if c.isalpha() else c
        for c in text.lower()
        if c.isalnum()
    )


def transcode_preset(transform, n_chars=0):
    return partial(transcode, with_spaces(n_chars), transform)


encode = transcode_preset(lambda i, a, b: i * a + b, 5)
decode = transcode_preset(lambda i, a, b: (i - b) * mmi(a))
