def antyfunc(counter, mypoints, enpoints, mylist, enlist):
    if counter > 150: return "d"
    if not "c" in enlist[-2:]:
        return "d"
    if enpoints >= mypoints:
        return "d"
    else:
        return "c"
