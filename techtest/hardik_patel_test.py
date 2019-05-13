from QueA import isOverlapping
from Que2 import newerThan

def overlapTest():
    success = True

    if isOverlapping(1, 2, 3, 4) != False:
        success = False
        print('expected ' + False + ' but got ' + (isOverlapping(1, 2, 3, 4)))
    if isOverlapping(1, 3, 2, 4) != True:
        success = False
        print('expected ' + True + ' but got ' + (isOverlapping(1, 3, 2, 4)))
    if isOverlapping(3, 4, 1, 2) != False:
        success = False
        print('expected ' + False + ' but got ' + (isOverlapping(3, 4, 1, 2)))
    if isOverlapping(2, 4, 1, 3) != True:
        success = False
        print('expected ' + True + ' but got ' + (isOverlapping(2, 4, 1, 3)))
    if isOverlapping(2, 3, 1, 4) != True:
        success = False
        print('expected ' + True + ' but got ' + (isOverlapping(2, 3, 1, 4)))
    if isOverlapping(1, 4, 2, 3) != True:
        success = False
        print('expected ' + True + ' but got ' + (isOverlapping(1, 4, 2, 3)))
    if isOverlapping(1, 3, 1, 2) != True:
        success = False
        print('expected ' + True + ' but got ' + (isOverlapping(1, 3, 1, 2)))
    if isOverlapping(1, 4, 2, 4) != True:
        success = False
        print('expected ' + True + ' but got ' + (isOverlapping(1, 4, 2, 4)))

    if success:
        print('All overlapping tests successfully performed.\n')
    else:
        print('All overlapping tests performed. (With errors)\n')


def versionTest():
    success = True

    if newerThan('1', '2') != -1:
        success = False
        print(newerThan('1', '2'))
    if newerThan('1.1', '1.2') != -1:
        success = False
        print(newerThan('1.1', '1.2'))
    if newerThan('1.3', '1.3.1') != -1:
        success = False
        print(newerThan('1.3', '1.3.1'))
    if newerThan('1.4', '1.3.12') != 1:
        success = False
        print(newerThan('1.4', '1.3.12'))
    if newerThan('3.1.1', '3.1.10') != -1:
        success = False
        print(newerThan('3.1.1', '3.1.10'))
    if newerThan('3.1.1.4321', '3.1.1.4321') != 0:
        success = False
        print(newerThan('3.1.1.4321', '3.1.1.4321'))
    if newerThan('2', '1') != 1:
        success = False
        print(newerThan('2', '1'))
    if newerThan('4.2', '1.2') != 1:
        success = False
        print(newerThan('4.2', '1.2'))
    if newerThan('1.1', '2') != -1:
        success = False
        print(newerThan('1.1', '2'))
    if newerThan('3.1.3', '3.1.3') != 0:
        success = False
        print(newerThan('3.1.3', '3.1.3'))
    if newerThan('1', '1.1.12.4444') != -1:
        success = False
        print(newerThan('1', '1.1.12.4444'))

    if success:
        print('All version tests successfully performed.\n')
    else:
        print('All version tests performed. (With errors)\n')


print('Test for Question A: Overlapping lines')
overlapTest()

print('Test for Question B: Version check')
versionTest()
