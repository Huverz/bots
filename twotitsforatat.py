def twotitsforatatfunc(num, mypoints, enpoints, myhistory, enhistory):
    if num == 0 or num==1 and enhistory[-1]=="c":
        return "c"
    if enhistory[-1] == "d" or enhistory[-2] == "d" or num >= 195:
        return "d"
    else:
        return "c"
