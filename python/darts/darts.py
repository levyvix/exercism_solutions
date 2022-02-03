import math


def score(x, y):
    """The outer circle has a radius of 10 units (This is equivalent to the 
    total radius for the entire target), the middle circle a radius of 5 units, 
    and the inner circle a radius of 1. Of course, they are all centered to the same point 
    (That is, the circles are concentric) defined by the coordinates (0, 0).
    """

    # distance from center
    d = math.sqrt((x ** 2) + (y ** 2))

    if d <= 1:
        return 10
    elif d <= 5:
        return 5
    elif d <= 10:
        return 1
    else:
        return 0
