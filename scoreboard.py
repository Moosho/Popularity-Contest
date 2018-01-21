from collections import Counter


class scoreboard():
    """Scores values given to it based on theyr frequency."""

    def __init__(self, *arg):
        self.urls = []
        self.scored = None
        for x in arg:
            self.urls += x
        pass

    def show(self):
        return self.board(self.score())

    def score(self):
        c = Counter()
        for x in self.urls:
            c[x] += 1
        self.scored = c.most_common()
        return self.scored

    def board(self, scoredDomains):
        for domain in range(len(scoredDomains)):
            print("{} Hit(s) on {}".format(
                scoredDomains[domain][1], scoredDomains[domain][0]))
            pass
        pass
