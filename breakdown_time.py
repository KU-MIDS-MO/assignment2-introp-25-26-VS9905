def breakdown_time(seconds):
    if type(seconds) != int or seconds < 0:
        return -1
    if seconds == 0:
        return {}

    fdic = {}
    for i in [3600,60,1]:
        if seconds >= i:
            a = seconds // i
            seconds = seconds % i
            fdic[i] = a
    return fdic



