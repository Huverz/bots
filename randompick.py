from random import choice

def randompickfunc(counter, mypoints, enpoints, mylist, enlist):
    if counter == 199:
        return "d"
    else:
        return choice(["d", "c"])
