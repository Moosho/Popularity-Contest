from website import website
from scoreboard import scoreboard

list_of_them_all = []
print("Working...")
w = website()
w.start()
ex = w.getExternalLinks()
list_of_them_all += ex
print("This is {} domain.\nAnd these are it's external links: {}".format(w.getDomain(), ex))
for x in ex:
    w = website(domain=x)
    w.start()
    ex = w.getExternalLinks()
    list_of_them_all += ex
    print("This is {} domain.\nAnd these are it's external links: {}".format(w.getDomain(), ex))
    for x in ex:
        w = website(domain=x)
        w.start()
        ex = w.getExternalLinks()
        list_of_them_all += ex
        print("This is {} domain.\nAnd these are it's external links: {}".format(w.getDomain(), ex))
print("\nAll external links found:\n{}".format(list_of_them_all))
