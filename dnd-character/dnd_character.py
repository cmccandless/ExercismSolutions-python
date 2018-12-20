from random import randint


ABILITIES = [
    'strength',
    'dexterity',
    'constitution',
    'intelligence',
    'wisdom',
    'charisma',
]


def modifier(score):
    return (score - 10) // 2


def roll(count=1, drop=0, sides=6):
    return sum(sorted(randint(1, sides) for _ in range(count))[drop:])


class Character:
    def __init__(self):
        for ability_name in ABILITIES:
            setattr(self, ability_name, self.ability())
        self.hitpoints = modifier(self.constitution) + 10

    def ability(self):
        return roll(4, drop=1)
