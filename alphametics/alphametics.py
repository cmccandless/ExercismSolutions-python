from itertools import permutations


def sub(solution, word):
    if solution[word[0]] == '0':
        raise ValueError()
    return int(''.join(solution.get(w, w) for w in word))


def solve(expr):
    words = [w for w in expr.split() if w not in ['+', '==']]
    letters = {ch for ch in expr if ch not in '+= '}
    for solution in (dict(zip(letters, perm)) for perm in
                     permutations('9876543210', len(letters))):
        try:
            *left, right = (sub(solution, word) for word in words)
            if sum(left) == right:
                return {k: int(v) for k, v in solution.items()}
        except ValueError:
            pass
    return {}
