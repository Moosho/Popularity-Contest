# Plan of how to structure this program.
# Scoreboard
# Website
# Random domain name generator
import random
import string
import requests
import bs4
import re


class Website():
    """Menages getting a domain, checks if it's working and gets it's HTML."""

    def __init__(self, length, firstLevelDomain="com", url=False):
        self.header_dict = {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
            "Accept-Encoding": "gzip, deflate",
            "Accept-Language": "en-US,en;q=0.9,pl-PL;q=0.8,pl;q=0.7",
            "Referer": "https://www.google.pl/",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36"
        }
        self.length = length
        self.firstLevelDomain = str(firstLevelDomain)
        self.domain = None
        self.html = None
        self.extLinksList = None

# TODO: make that it has limited amount of tries and if exceeded raise exception.
# TODO: if website gets only url var, skip all the random and checking stuff
        while True:
            self.rand_domain()
            resp = self.request_domain()
            if resp is False:
                continue
            self.html = resp
            self.extLinksList = self.extLinks()
            break
        print("Domain: {}\nHtml: {}".format(self.domain, self.html))

    def rand_domain(self):
        name = ""
        for n in range(int(self.length)):
            randLetter = random.choice(string.ascii_lowercase)
            name = "{}{}".format(name, randLetter)
        self.domain = "http://{}.{}".format(name, self.firstLevelDomain)

    def request_domain(self):
        try:
            rq = requests.request("GET", str(self.domain), headers=self.header_dict)
        except Exception as e:
            print(e)
            return False
        return rq.text

    def extLinks(html):
        bs = bs4.BeautifulSoup(html, "html.parser")
        links = []
        for a_tag in bs.find_all("a"):
            href = a_tag.get("href")
            try:
                result = re.match(r'htt(p|ps)://.+\.com/?', str(href))
            except Exception as e:
                print("{} piperol".format(e))
            if result is None:
                continue
            else:
                links.append(result)
        return links


w = Website(3, "com")
