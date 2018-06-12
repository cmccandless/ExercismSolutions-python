class Clock:
    def __init__(self, hour, minute):
        self.minutes = 0
        self.__add__(hour * 60 + minute)

    def __add__(self, minutes):
        self.minutes += minutes
        while self.minutes < 0:
            self.minutes += 1440
        self.minutes %= 1440
        return self

    def __sub__(self, minutes):
        return self + -minutes

    def __str__(self):
        return '{:02}:{:02}'.format(*divmod(self.minutes, 60))

    def __eq__(self, other):
        return self.minutes == other.minutes
