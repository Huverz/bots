import random
def handshakefunc(num, me, him, m, en):
    handshake = "cdccd"
    # For the first few rounds, give the handshake.
    if num < len(handshake):
        if m == en:
            return handshake[num]
        return "d"
    if en[:len(handshake)] == handshake:
        if me > him:
            return "d"
        if me == him:
            return "ccd"[random.randint(0,2)]
        return "c"
    return "d"
