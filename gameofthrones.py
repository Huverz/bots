def gameofthronesfunc(counter, mypoints, enpoints, mylist, enlist):
    turn_to_betray = 140
    if counter >= turn_to_betray or mypoints > enpoints or "d" in enlist:
        return "d"
    else:
        return "c"
