class scoreboard():
    """Scores values given to it based on theyr frequency."""

    def __init__(self, *arg):
        self.urls = []
        for x in arg:
            self.urls += x
        pass
