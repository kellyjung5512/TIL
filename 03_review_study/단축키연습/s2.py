def gogo():
    print("GOGO")
    return


def abc():
    print("abc start")
    bts()
    gogo()
    print("abc finish")
    return


def bts():
    print("bts start")
    gogo()
    print("bts finish")
    return


gogo()
abc()
bts()