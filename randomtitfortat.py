import os
def randomtitfortatfunc(forgot, ten, var, iables, enlist):
    luck = enlist.count("d")
    choice = ord(os.urandom(1))
    choice = int(round(luck * float(choice - 0) / 255.0))
    if choice == 0:
        return "c"
    return "d"
