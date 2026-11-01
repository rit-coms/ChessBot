"""
does the math to determine angles and distances of the arms based on loactaions of everything

AUTHOR: Viraaj Gupta
"""
from math import *

#Chess board rn is 80x80, [0,0] is bottom left and the bot is in the middle and 40x40 footprint with the leadscrew in the middle
SQUARE_SIZE = 10
SCREW_OFFSET = 20
SCREW_LOCATION = [40,-20]
#Total straight arm length = sqrt(95^2 + 35^2) = 101.24228365658293466623451144951
UPPER_ARM = 50.621141828291467333117255724753
FOREARM = 50.621141828291467333117255724753

def sqr_to_crds(sqr):
    """
    converts square coords to cartesian coords
    square coords: bottom left is [1,1] and top right is [8,8]
    cartesian coords: points to the middle of a square
    """
    return [(sqr[0]-1)*SQUARE_SIZE + SQUARE_SIZE/2, (sqr[1]-1)*SQUARE_SIZE + SQUARE_SIZE/2]

def distance_and_angle(sqr):
    """
    Distance between lead screw and input square
    """
    x = sqr_to_crds(sqr)[0] - SCREW_LOCATION[0]
    y = sqr_to_crds(sqr)[1] - SCREW_LOCATION[1]
    dist = sqrt(x**2 + y**2)
    angle = atan(x/y)
    return [dist, angle]

#Formula for forearm and upperarm is based on law of cosines

def forearm(len):
    """
    angle of forearm relative to upperarm tangent (like basically how much the turtle should turn)(aka outer angle?)
    """
    a = FOREARM
    b = UPPER_ARM
    c = len if len <= a+b else a+b
    return acos((a**2 + b**2 - c**2)/(2*a*b)) #Returns in radians

def upperarm(len):
    """
    returns angle of upper arm relative to angle of shortest line from lead screw to square in one line
    """
    a = FOREARM
    b = UPPER_ARM
    c = len if len <= a+b else a+b
    return acos((b**2 + c**2 - a**2)/(2*b*c))

def main():
    """
    asks square numbers (bottom left is [1,1] and top right is [8,8])
    prints distance, angle of shortest line from lead screw to square in one line
    prints angle of upper arm relative to angle of shortest line from lead screw to square in one line
    prints angle of forearm relative to upperarm tangent (like basically how much the turtle should turn)(aka outer angle?)
    """
    distnangl = distance_and_angle([int(input("Input square x: ")),int(input("Input square y: "))])
    print(distnangl[0],distnangl[1]/pi*180)
    print(upperarm(distnangl[0])/pi*180)
    print(forearm(distnangl[0])/pi*180)

if __name__ == "__main__":
    main()