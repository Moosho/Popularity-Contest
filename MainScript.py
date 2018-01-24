from website import website
from scoreboard import scoreboard
import threading

exlGlobal = []
tlist = []
lock = threading.Lock()
threads = 5


def gel(web):
    global exlGlobal
    w = website(domain=web)
    w.start()
    exlGlobal += w.getExternalLinks()


print("Start of the program...")

w = website(domain="http://www.vb.com")
w.start()
exlGlobal += w.getExternalLinks()

if exlGlobal == []:
    print("No external links have been found on the root domain {}".format(w.getDomain()))
else:

    print("Root domain: {}\nLinks form first random domain: {}".format(w.getDomain(), exlGlobal))

    for x in range(len(exlGlobal)):
        thread = threading.Thread(target=gel, args=(exlGlobal[x],))
        with lock:
            print(exlGlobal[x])
        thread.daemon = True
        thread.start()
        thread.join()

    sb = scoreboard(exlGlobal)
    # print(sb.score())
    print("\n")
    sb.show()
