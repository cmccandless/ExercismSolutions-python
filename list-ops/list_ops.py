# Please, do not use the built-in python functions like map, reduce, len, etc.
# that solve the same problems and try to solve it yourself instead.


def foldl(function, xs, acc):
    for x in xs:
        acc = function(acc, x)
    return acc


def append(xs, ys, extend=True):
    if isinstance(ys, list) and extend:
        return foldl(lambda a, b: append(a, b, False), ys, xs)
    xs.append(ys)
    return xs


def foldr(function, xs, acc):
    while length(xs):
        acc = function(xs.pop(), acc)
    return acc


def map_clone(function, xs):
    return foldl(lambda a, b: append(a, function(b)), xs, [])


def length(xs):
    return foldl(lambda a, b: a + 1, xs, 0)


def filter_clone(function, xs):
    return foldl(lambda a, b: append(a, b) if function(b) else a, xs, [])


def reverse(xs):
    return foldr(lambda b, a: append(a, b, False), xs, [])


def concat(*args):
    return foldl(lambda a, b: foldl(append, b, a), args, [])
