from math import sqrt


def score(x, y):
    distance = sqrt(x * x + y * y)
    for circle, points in [(1, 10), (5, 5), (10, 1)]:
        if distance <= circle:
            return points
    return 0
