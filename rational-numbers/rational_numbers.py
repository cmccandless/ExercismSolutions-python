from __future__ import division
try:
    from math import gcd
except ImportError:
    from fractions import gcd


class Rational(object):
    def __init__(self, numer, denom):
        _gcd = gcd(numer, denom)
        self.numer = numer // _gcd
        self.denom = denom // _gcd
        if self.denom < 0:
            self.denom *= -1
            self.numer *= -1

    def __eq__(self, other):
        return self.numer == other.numer and self.denom == other.denom

    def __repr__(self):
        return '{}/{}'.format(self.numer, self.denom)

    def __add__(self, other):
        return Rational(
            self.numer * other.denom + other.numer * self.denom,
            self.denom * other.denom
        )

    def __sub__(self, other):
        return Rational(
            self.numer * other.denom - other.numer * self.denom,
            self.denom * other.denom
        )

    def __mul__(self, other):
        return Rational(
            self.numer * other.numer,
            self.denom * other.denom
        )

    def __truediv__(self, other):
        return Rational(
            self.numer * other.denom,
            self.denom * other.numer
        )

    def __abs__(self):
        if self.numer < 0:
            return Rational(-self.numer, self.denom)
        return self

    def __pow__(self, power):
        return Rational(
            self.numer ** power,
            self.denom ** power
        )

    def __rpow__(self, base):
        return (base ** (1.0 / self.denom)) ** self.numer
