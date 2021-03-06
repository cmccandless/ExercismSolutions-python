animal = ['fly', 'spider', 'bird', 'cat', 'dog', 'goat', 'cow', 'horse']
spider = ' wriggled and jiggled and tickled inside her'
extra = [
    '',
    'It{}.'.format(spider),
    'How absurd to swallow a bird!',
    'Imagine that, to swallow a cat!',
    'What a hog, to swallow a dog!',
    'Just opened her throat and swallowed a goat!',
    'I don\'t know how she swallowed a cow!',
    'She\'s dead, of course!'
]


def phrase(n_verse):
    phrase = 'She swallowed the {} to catch the {}{}.'
    phrase = phrase.format(
        animal[n_verse],
        animal[n_verse - 1],
        ' that{}'.format(spider) if n_verse == 2 else ''
    )
    return phrase


def verse(n_verse):
    if n_verse != int(n_verse):
        return ['']
    n_verse = int(n_verse)
    lst = ['I know an old lady who swallowed a {}.'.format(animal[n_verse])]
    if n_verse > 0:
        lst.append(extra[n_verse])
    if n_verse < 7:
        lst.extend(phrase(n) for n in range(n_verse, 0, -1))
        lst.append("I don't know why she swallowed the fly. "
                   "Perhaps she'll die.")
    return lst


def rangef(start, stop, step=0.5):
    while start < stop:
        yield start
        start += step


def recite(start, stop):
    return [
        (line, print(line))[0]
        for i in rangef(start - 1, stop - 0.5)
        for line in verse(i)
    ]
