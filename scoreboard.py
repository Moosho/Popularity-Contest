from collections import Counter


class scoreboard():
    """Scores values given to it based on theyr frequency."""

    def __init__(self, *arg):
        self.urls = []
        self.scored = None
        for x in arg:
            self.urls += x
        pass

    def score(self,):
        c = Counter()
        for x in self.urls:
            c[x] += 1
        self.scored = c.most_common()
        return self.scored
