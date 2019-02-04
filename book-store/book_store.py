from functools import reduce
from itertools import groupby

BASE_COST = 800
discount = [1.0, 1.0, 0.95, 0.9, 0.8, 0.75]


# def groupCost(g):
#     return len(g) * discount[len(g)]


# class Grouping:
#     def __init__(self, groups=[set()]):
#         self.groups = groups

#     def total(self):
#         return sum(map(groupCost, self.groups)) * BASE_COST

#     def dup(self):
#         return Grouping(list(map(set, self.groups)))

#     def add(self, b, index=0):
#         other = self.dup()
#         other.groups.sort(key=lambda g: len(g))
#         valid = list(filter(lambda g: b not in g, other.groups))
#         if len(valid) == 0:
#             other.groups.append(set([b]))
#         else:
#             valid[index].add(b)
#         return other

#     def __lt__(self, other):
#         return self.total() < other.total()


# def step(t, b):
#     sm, la = t
#     return (min(sm.add(b), la.add(b)), min(sm.add(b, -1), la.add(b, -1)))


# def calculate_total(books):
#     if len(books) == 0:
#         return 0
#     start = Grouping().add(books[0])
#     return round(min(reduce(step, books[1:], (start, start.dup()))).total())

class Grouping(object):
    @classmethod
    def start(cls, book):
        return cls([[book]])

    def __init__(self, groups):
        self.groups = groups

    def total(self):
        return sum(len(g) * discount[len(g)] for g in self.groups)

    def dup(self):
        return self.__class__([list(g) for g in self.groups])

    def add_to_all(self, book):
        other = self.dup()
        other.groups.append([book])
        results = [other]
        for i, group in enumerate(self.groups):
            if book in group:
                continue
            o = self.dup()
            o.groups[i].append(book)
            results.append(o)
        return results

    def __lt__(self, other):
        return self.total() < other.total()

    def __len__(self):
        return len(self.groups)


def get_group_count(books):
    return max(len(list(g)) for _, g in groupby(books))


def get_groupings(books):
    def reduction(groupings, book):
        return [
            g
            for gs in groupings
            for g in gs.add_to_all(book)
            if len(g) <= num_groups
        ]

    num_groups = get_group_count(books)
    return reduce(
        reduction, books, [Grouping.start(books.pop(0))]
    )


def calculate_total(books):
    if not books:
        return 0
    return round(BASE_COST * min(get_groupings(sorted(books))).total())
