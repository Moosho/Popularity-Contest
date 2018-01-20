#
#       ---POPULARITY CONTEST---
#  Find random 4 letter .com websites and grab all axternal links to other domains.
#  Then core found domains based on how many times have they been found on different websites.
#
import requests as rq
import random
import string
import re
from urllib import parse
from bs4 import BeautifulSoup as bs
from collections import Counter


def domains(how_many_domains, how_many_letters):

    # Searches for domains made up of random letters with the specifications provided.
    # Returns a list of valid web urls.

    domains_found = []

    while len(domains_found) < int(how_many_domains):
        d = ""
        for n in range(how_many_letters):
            randLetter = random.choice(string.ascii_lowercase)

            d += randLetter
            pass
        try:
            r = rq.request("GET", "http://{}.com".format(d))
        except Exception as e:
            # IGNORE
            continue
        if r.ok:
            domains_found.append(r.url)
            print("Found {} valid domain(s)".format(len(domains_found)))

    return domains_found


def findLinks(web_addresses, square=False):
    # squere is here as thing to do in future. If set to True it will search for links in links found in the first search rom roandom letters

    # Finds every external url link from a provided website.

    header_dict = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "en-US,en;q=0.9,pl-PL;q=0.8,pl;q=0.7",
        "Referer": "https://www.google.pl/",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36"
    }

    my_pattern = re.compile(r'htt(p|ps)://.+\.com/?')
    htmls = []
    html_links = []

    for a in web_addresses:
        # All adresses bust be valid (Must contain html).
        # Get htmls form adresses given and store them in a htmls list
        try:
            r = rq.request("GET", a, headers=header_dict)
        except Exception as e:
            print("{} Dinopipol".format(e))
            continue
        htmls.append(r.text)

    x = 0  # index website url in web_addresses
    for html in htmls:
        local_links = []
        # Find string values of href's found in the site's html
        html_bs = bs(html, "html.parser")
        print("searching for links in {}\n".format(web_addresses[x]))

        for a_tag in html_bs.find_all("a"):
            href = a_tag.get("href")
            try:
                result = re.match(my_pattern, str(href))
            except Exception as e:
                print("{} piperol".format(e))

            if result is None:
                continue
            if result.group(0) == web_addresses[x]:
                continue
            if result.group(0) in local_links:
                continue

            local_links.append(result.group(0))
        x += 1
        html_links += local_links
        # print("All links gathered {}\n", format(html_links))
    return html_links


def ranking(links, how_many_x):
    # _-> to dict: Websire - times it appeared
    # sort descending
    # print it in a table per row below a heading
    how_many = how_many_x
    links_pa = []
    for link in links:
        parsed = parse.urlparse(link)
        links_pa.append("{}".format(parsed.netloc))

    links_co = Counter()
    for link in links_pa:
        links_co[link] += 1

    links_co_desc_list = links_co.most_common(how_many)
    print(links_co_desc_list)
    if how_many > len(links_co_desc_list):
        how_many = len(links_co_desc_list)

    print("All scored links {}\n", format(links_co.most_common()))

    print("""
#############################
#### Popularity contest #####
######### TOP {} ############
#############################""".format(how_many))

    x = 0
    while x < how_many:
        for l in links_co_desc_list:
            print("{} Hit(s) on {}".format(links_co_desc_list[x][1], links_co_desc_list[x][0]))
            x += 1


print("Working...")
# print(findLinks(["http://goh.com/", "https://www.seo.com/", "http://ww4.goj.com", "http://teb.pl/"]))
print(ranking(findLinks(domains(50, 3)), 15))
