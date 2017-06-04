import os
def randomchoicev2func(num, i, d, c, enlist):
    lucky = ord(os.urandom(1))
    lucky = int(round(float(lucky) / 255.0))
    if (lucky == 0 or num == 0) and num != 199:
        return "c"
    return "d"
