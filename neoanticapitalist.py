def neoanticapitalistfunc(counter, mypoints, enpoints, mylist, enlist):
    if mypoints >= enpoints:
        if counter > 1:
            if counter == 199 or (enlist[-1] != "c" and enlist[-2] != "c"):
                return "d"
        return "c"
    else:
        return "d"
