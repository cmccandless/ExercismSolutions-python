from functools import reduce, partial


class Item(object):
    @classmethod
    def zero(cls):
        return cls(0, 0)

    def __init__(self, weight, value):
        self.weight = weight
        self.value = value

    def __add__(self, other):
        return self.__class__(
            self.weight + other.weight,
            self.value + other.value,
        )

    def matches(self, row, target_weight):
        return (
            self.weight <= target_weight and
            self.value > row[target_weight].value
        )


def reducer(max_weight, current_row, item):
    new_row = list(current_row)
    for target_weight in range(item.weight, max_weight + 1):
        subitem = current_row[target_weight - item.weight] + item
        if subitem.matches(current_row, target_weight):
            new_row[target_weight] = subitem
    return new_row


def solve_knapsack(max_weight, items):
    return reduce(
        partial(reducer, max_weight),
        (Item(**i) for i in items),
        [Item.zero()] * (max_weight + 1)
    )[-1].value
