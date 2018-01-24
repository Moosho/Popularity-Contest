from website import website
from scoreboard import scoreboard
from queue import Queue
import threading

exlGlobal = []
q = Queue()
lock = threading.Lock()
threads = 5


def gel(web):
    global exlGlobal
    w = website(domain=web)
    w.start()
    with lock:
        print(w.getExternalLinks)
        exlGlobal += w.getExternalLinks()


def threader():
    website = q.get()
    gel(website)
    q.task_done()
    pass


print("Working...")

w = website(2, guesses=1000)
w.start()
exlGlobal += w.getExternalLinks()

if exlGlobal == []:
    print("No external links have been found on the root domain {}".format(w.getDomain()))
else:

    print("{}\nLinks form first random domain: {}".format(w.getDomain(), exlGlobal))

    for w in exlGlobal:
        print(w)
        q.put(w)

    for x in range(threads):
        thread = threading.Thread(target=threader)
        thread.daemon = True
        thread.start()

    q.join
    sb = scoreboard(exlGlobal)
    # print(sb.score())
    print("\n")
    sb.show()
