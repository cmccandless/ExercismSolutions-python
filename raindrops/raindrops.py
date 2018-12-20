def raindrops(number):
    return ''.join((
        'Pling' if number % 3 == 0 else '',
        'Plang' if number % 5 == 0 else '',
        'Plong' if number % 7 == 0 else '',
    )) or str(number)
