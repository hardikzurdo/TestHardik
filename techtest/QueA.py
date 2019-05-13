# I will make the assumption that x1 is always smaller than x3
# I will make the assumption that x2 >= x1 and x4 >= x3
# Returns true if overlapping, False otherwise
def isOverlapping(x1, x2, x3, x4):
    if x1 < x3 and x2 <= x3:
        return False
    elif x1 < x3 and x2 >= x3:
        return True
    elif x3 <= x1 and x4 <= x1:
        return False
    elif x3 <= x1 and x4 >= x1:
        return True
