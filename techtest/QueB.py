# returns 1 if v1 is newer than v2,
# returns 0 if same version
# returns -1 if v1 is older than v2
def newerThan(v1, v2):
    x1 = v1.split('.')
    x2 = v2.split('.')

    if len(x1) < max(len(x1), len(x2)):
        x1 = x1 + [0] * (len(x2) - len(x1))
    elif len(x2) < max(len(x1), len(x2)):
        x2 = x2 + [0] * (len(x2) - len(x1))

    for i in range (0, len(x1)):
        if int(x1[i]) > int(x2[i]):
            return 1
        elif int(x1[i]) < int(x2[i]):
            return -1

    return 0
