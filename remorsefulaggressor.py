from random import randint
def remorsefulaggressorfunc(counter, mypoints, enpoints, mylist, enlist):
    if counter == 0:
        return "d"
    if (counter > 195 and mylist[len(enlist)-1] == "d"):
        return "d"
    if ((counter == 1 or counter > 2) and enlist[len(enlist)-1] == "d"):
        return "d"
    if (counter == 2 and enlist[len(enlist)-1] == "d" and enlist[len(enlist)-2] == "d"):
        return "d"
    if (counter >= 195 and randint(0, 200 - counter) == 0):
        return "d"
    else:
        return "c"
