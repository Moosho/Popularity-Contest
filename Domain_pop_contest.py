# Scoreboard
# Website
# Random domain name gen
import random
import string
import requests


class Website():
    """Menages getting a domain, checking if it's working and gets it's HTML."""

    def __init__(self, length, firstLevelDomain):
        self.length = length
        self.firstLevelDomain = str(firstLevelDomain)
        self.domain = None
        self.html = None

# TODO: make that it has limited amount of tries and if exceeded raise exception
        while True:
            self.rand_dom()
            resp = self.request_domain()
            if resp is False:
                continue
            self.html = resp
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


class Links():
    """Extracts all external links from a given HTML, aside of self refferencing ones."""

    def __init__(self, raw_html):
        self.raw_html = raw_html


w = Website(3, "com")
