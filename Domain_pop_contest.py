# Plan of how to structure this program.
# Scoreboard
# Website
# Random domain name generator
import random
import string
import requests


class Website():
    """Menages getting a domain, checks if it's working and gets it's HTML."""

    def __init__(self, length, firstLevelDomain="com", url=False):
        self.length = length
        self.firstLevelDomain = str(firstLevelDomain)
        self.domain = None
        self.html = None
        self.extLinksList = None

# TODO: make that it has limited amount of tries and if exceeded raise exception.
# TODO: if website gets only url var, skip all the random and checking stuff
        while True:
            self.rand_dom()
            resp = self.request_domain()
            if resp is False:
                continue
            self.html = resp
            self.extLinksList = self.extLinks()
            break
        print("Domain: {}\nHtml: {}".format(self.domain, self.html))

    def rand_dom(self):
        name = ""
        for n in range(int(self.length)):
            randLetter = random.choice(string.ascii_lowercase)
            name = "{}{}".format(name, randLetter)
        self.domain = "http://{}.{}".format(name, self.firstLevelDomain)

    def request_domain(self):
        try:
            rq = requests.request("GET", str(self.domain))
        except Exception as e:
            print(e)
            return False
        return rq.text

    def extLinks(html):
        pass


w = Website(3, "com")
