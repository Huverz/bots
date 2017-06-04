from random import randint
def luckytitfortatfunc(num, i, d, mylist, enlist):
    lucky = randint(0, 200)
    if lucky == 0:
        return "c"
    if num == 0 or enlist[-1] == "c":
        return "c"
    else:
        return "d"
