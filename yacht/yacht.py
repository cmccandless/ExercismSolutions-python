from collections import Counter

# Score categories
YACHT = 0
ONES = 1
TWOS = 2
THREES = 3
FOURS = 4
FIVES = 5
SIXES = 6
FULL_HOUSE = 7
FOUR_OF_A_KIND = 8
LITTLE_STRAIGHT = 9
BIG_STRAIGHT = 10
CHOICE = 11


def sum_only(dice, die):
    return sum(d for d in dice if d == die)


def score(dice, category):
    for die, cat in enumerate([ONES, TWOS, THREES, FOURS, FIVES, SIXES], 1):
        if cat and category == cat:
            return sum_only(dice, die)
    for start, cat in enumerate((LITTLE_STRAIGHT, BIG_STRAIGHT), 1):
        if category == cat:
            if sorted(dice) == list(range(start, start + 5)):
                return 30
            else:
                break
    if category == FULL_HOUSE:
        if set(Counter(dice).values()) == {2, 3}:
            return sum(dice)
    elif category == FOUR_OF_A_KIND:
        counts = Counter(dice)
        for d, c in counts.items():
            if c >= 4:
                return 4 * d
    elif category == CHOICE:
        return sum(dice)
    elif category == YACHT:
        if dice == [dice[0]] * 5:
            return 50
    for start, cat in enumerate((LITTLE_STRAIGHT, BIG_STRAIGHT), 1):
        if category == cat:
            if sorted(dice) == list(range(start, start + 5)):
                return 30
            else:
                break
    for die, cat in enumerate([ONES, TWOS, THREES, FOURS, FIVES, SIXES], 1):
        if cat and category == cat:
            return sum_only(dice, die)
    return 0
