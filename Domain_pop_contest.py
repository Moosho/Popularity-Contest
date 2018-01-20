import random
import string
import requests
import bs4
import re
from urllib import parse


class Website():
    """Menages getting a domain, checks if it's working and gets it's HTML."""

    def __init__(self, length, firstLevelDomain="com", tries=50, domain=None):
        self.header_dict = {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
            "Accept-Encoding": "gzip, deflate",
            "Accept-Language": "en-US,en;q=0.9,pl-PL;q=0.8,pl;q=0.7",
            "Referer": "https://www.google.pl/",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36"
        }
        self.length = length
        self.firstLevelDomain = firstLevelDomain
        self.tries = tries
        self.domain = domain
        self.html = ""
        self.extLinksList = []

        # Logic
        if self.domain is None:
            for x in range(self.tries):
                dom = self.rand_domain()
                self.domain = dom

                resp = self.request_domain()
                self.html = str(resp)
                if resp is False:
                    continue
        else:
            self.html = self.request_domain(self.domain)
        # print("Domain:\n{}\nHtml:\n{}\n".format(self.domain, self.html))
        html_raw = self.html
        ext = self.extLinks(html_raw)
        print("HTML:\n{}\n\n\nqqqqqqqqqqqqqq {}".format(self.html, ext))
        print(ext)
        print(self.domain)

    def rand_domain(self):
        name = ""
        for n in range(int(self.length)):
            randLetter = random.choice(string.ascii_lowercase)
            name = "{}{}".format(name, randLetter)
        return "http://www.{}.{}".format(name, self.firstLevelDomain)

    def request_domain(self, url=None):
        if url is None:
            url = self.domain
        try:
            rq = requests.request("GET", url, headers=self.header_dict)
        except Exception as e:
            print(e)
            print("aaaaaaaaaaaaaaaaaa")
            return False
        return rq.text

    def extLinks(self, html):
        bs = bs4.BeautifulSoup(html, "html.parser")
        links = []
        for a_tag in bs.find_all("a"):
            href = a_tag.get("href")
            try:
                result = re.match(r'htt(p|ps)://.+\.com/?', str(href))
            except Exception as e:
                print(e)
                continue
            if result is None:
                continue
            lp = parse.urlparse(str(result.group(0)).lower())
            if lp == parse.urlparse(self.domain):
                continue
            else:
                links.append(lp.netloc)
        return links


w = Website(3, "com", domain="http://www.nfl.com")
