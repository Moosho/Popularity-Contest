from website import website
from scoreboard import scoreboard
from queue import Queue
import threading

exlGlobal = []
tlist = []
lock = threading.Lock()
q = Queue()
threads = 5


def gel(web):
    global exlGlobal
    with lock:
        print(web)
    w = website(domain=web)
    w.start()
    exlGlobal += w.getExternalLinks()


def threader():
    while True:
        if q.empty() is True:
            break
        domain = q.get()
        gel(domain)
        q.task_done()


print("Start of the program...")
w = website(length=3, guesses=50)
w.start()
exlGlobal += w.getExternalLinks()

if exlGlobal == []:
    print("No external links have been found on the root domain {}".format(w.getDomain()))
else:

    print("Root domain: {}\nLinks form first random domain: {}".format(w.getDomain(), exlGlobal))

    for domain in range(len(exlGlobal)):
        q.put(exlGlobal[domain])

    for thread in range(5):
        t = threading.Thread(target=threader)
        t.deamon = True
        t.start()

    q.join()
    sb = scoreboard(exlGlobal)
    # print(sb.score())
    print("\n")
    sb.show()
