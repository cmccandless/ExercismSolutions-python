FMT_REPORT = (
    "Your latest score was {latest}. "
    "That's {qualifier}your personal best!"
)


class HighScores(object):
    def __init__(self, scores):
        self.scores = scores

    def highest(self):
        return max(self.scores)

    def latest(self):
        return self.scores[-1]

    def top(self):
        return sorted(self.scores, reverse=True)[:3]

    def report(self):
        diff = self.highest() - self.latest()
        return FMT_REPORT.format(
            latest=self.latest(),
            qualifier=(
                '{} short of '.format(diff)
                if diff != 0 else
                ''
            )
        )
