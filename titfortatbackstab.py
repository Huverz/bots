from random import randint
def titfortatbackstabfunc(num, i, d, c, enlist):
    if num == 199:
        return "d";
    lucky = randint(0, 200)
    if lucky == 0:
        return "c"
    if num == 0 or enlist[num-1] == "c":
        return "c"
    else:
        return "d"
