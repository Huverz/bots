def teamerfunc(round, mypoints, enpoints, myhistory, enlist):
    if round == 0 or round == 4:
        return "c"
    elif round <= 5:
        return "d"
    if enlist[0-5] == "cdddcd":
        return "c"
    else:
        return "d"
