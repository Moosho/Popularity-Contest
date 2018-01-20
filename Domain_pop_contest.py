import random
import string
import requests
import bs4
import re
import tldextract


class website():
    """Menages getting a domain, checks if it's working and gets it's HTML."""

    def __init__(self, length=3, firstLevelDomain="com", guesses=50, domain=None):
        self.headers = {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
            "Accept-Encoding": "gzip, deflate",
            "Accept-Language": "en-US,en;q=0.9,pl-PL;q=0.8,pl;q=0.7",
            "Referer": "https://www.google.pl/",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36"
        }
        self.length = length
        self.firstLevelDomain = firstLevelDomain
        self.guesses = guesses
        self.domain = domain
        self.html = ""
        self.extLinksList = []

    def start(self):
        # Logic
        if self.domain is None:
            for x in range(self.guesses):

                # Optional debug print ----
                # print("Searching for a domain... Try NO. {}".format(x))

                dom = self.rand_domain()
                self.domain = dom

                resp = self.request_domain()
                if resp is False:

                    # Optional debug print ----
                    # print("Url {} has no website".format(self.domain))
                    continue
                self.html = str(resp)

                # Optional debug print ----
                # print("Url {} has a website".format(self.domain))
                break
        else:
            self.html = self.request_domain(self.domain)

        # optional debug print ----
        # print("Domain:\n{}\nHtml:\n{}\n".format(self.domain, self.html))

        self.extLinksList = self.extLinks(self.html)

        # Optional debug print that can raise a exception ----
        # try:
        #     print("HTML:\n{}\n\n\n{}".format(self.html, self.extLinksList))
        # except Exception as e:
        #     print(e)
        # ----

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
            rq = requests.request("GET", url, headers=self.headers, timeout=1)
        except Exception as e:
            print(e)
            return False
        return rq.text

    def extLinks(self, html):
        links = []
        try:
            bs = bs4.BeautifulSoup(html, "html.parser")
        except Exception as e:
            print(e)
        for a_tag in bs.find_all("a"):
            href = a_tag.get("href")
            try:
                result = re.match(r'htt(p|ps)://.+\.com/?', str(href))
            except Exception as e:
                print(e)
                continue
            if result is None:
                continue
            lp = tldextract.extract(str(result.group(0)).lower())
            dp = tldextract.extract(self.domain)

            # Optional debug print ----
            # Print pased domain that we check agains and our parsed and original url.
            # print("lp:  {}\ndp:  {}     Our domain original link:  {}\n".format(
            #     lp[1], dp[1], self.domain))
            # print(
            #     "Second check if the domain is already in our list. \nLink ---> {}\nList ---> {}\n".format(lp[1], links))
            # ----
            if lp[1] == dp[1]:
                continue
            elif lp[1] in links:
                continue
            else:
                links.append(lp[1])
        for x in range(len(links)):
            links[x] = "http://www.{}.com".format(links[x])
        return links

    def getExternalLinks(self):
        return self.extLinksList

    def getDomain(self):
        return self.domain

    def getHtml(self):
        return self.html


print("Working...")
w = website()
# w = Website(5, "com",)
w.start()
print(w.getExternalLinks())
print(w.getDomain())
# print(w.getHtml())
