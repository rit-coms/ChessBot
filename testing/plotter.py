"""
plots graph based on arm_angles.py

AUTHOR: Viraaj Gupta
"""
import turtle as t
import math
import arm_angles as aa

def init():
    """
    Generates chessboard and puts turtle at location of leadscrew
    """
    for i in range(8):
        for i in range(8):
            t.forward(aa.SQUARE_SIZE)
            t.left(90)
            t.forward(aa.SQUARE_SIZE)
            t.left(90)
            t.forward(aa.SQUARE_SIZE)
            t.left(90)
            t.forward(aa.SQUARE_SIZE)
            t.left(90)
            t.forward(aa.SQUARE_SIZE)
        t.penup()
        t.goto(0,t.pos()[1]+aa.SQUARE_SIZE)
        t.pendown()
    t.penup()
    t.goto(aa.SCREW_LOCATION)
    t.pendown()
    t.left(90)

def main():
    """
    asks square numbers (bottom left is [1,1] and top right is [8,8]) and then plots arms
    """
    init()
    inp = [int(input("Input square x: ")),int(input("Input square y: "))]
    inst = aa.distance_and_angle(inp)
    angle = inst[1]/math.pi*180
    upperarm_angle = aa.upperarm(inst[0])/math.pi*180
    forearm_angle = 180-aa.forearm(inst[0])/math.pi*180

    t.right(angle)
    if angle > 0:
        t.left(upperarm_angle)
    else:
        t.right(upperarm_angle)
    t.forward(aa.UPPER_ARM)
    if angle > 0:
        t.right(forearm_angle)
    else:
        t.left(forearm_angle)
    
    t.forward(aa.FOREARM)

if __name__ == "__main__":
    t.tracer(0, 0)
    main()
    t.update()
    t.done()