import re
def theelephantfunc(counter, mypoints, enpoints, mylist, enlist):
    interwoven = "".join(i for j in zip(mylist, enlist) for i in j)
    backwoven = interwoven[::-1]
    predict = re.match("^((?:..)*).*?(.).\\1(?:..)*$",backwoven)
    if(predict is None):
        return "c"
    predict = predict.groups()[1]
    if(predict == "d"):
        return "d"
    if(mypoints - enpoints >= 6):
        return "c"
    return "d"
 
