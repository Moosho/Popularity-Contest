from website import website
from scoreboard import scoreboard

list_of_them_all = []
print("Working...")
w = website(2, guesses=1000)
w.start()
ex = w.getExternalLinks()
list_of_them_all += ex
# print("Layer 1. This is {} domain.\nAnd these are it's external links: {}".format(w.getDomain(), ex))
for x in ex:
    w = website(domain=x)
    w.start()
    ex = w.getExternalLinks()
    list_of_them_all += ex
    # print("Layer 2. This is {} domain.\nAnd these are it's external links: {}".format(w.getDomain(), ex))
    for x in ex:
        w = website(domain=x)
        w.start()
        ex = w.getExternalLinks()
        list_of_them_all += ex
        # print("Layer 3. This is {} domain.\nAnd these are it's external links: {}".format(w.getDomain(), ex))
# print("\nAll external links found:\n{}".format(list_of_them_all))

sb = scoreboard(list_of_them_all)
# print(sb.score())
print("\n")
sb.show()
