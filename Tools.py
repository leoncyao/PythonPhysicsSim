"""Random Useful Functions"""
import math
def find_angle(pos1_x, pos1_y, pos2_x, pos2_y) -> float:
    """
    finds angle between pos1 and pos2, taking pos1 as origin
    >>> find_angle(0, 0, 5, 5)
    45 Degrees
    >>> find_angle(0, 0, -5, 5)
    135 Degrees
    >>> find_angle(0, 0, -5, -5)
    225 Degrees
    >>> find_angle(0, 0, 5, -5)
    315 Degrees
    """
    dx = pos2_x - pos1_x
    dy = pos2_y - pos1_y
    angle = 0
    if dx == 0:
        if dy > 0:
            angle = 0
        elif dy <= 0:
            angle = math.pi/2
    else:
        angle = math.atan(dy/dx)
        angle = abs(angle)

        if dx > 0 and dy > 0:
            angle = angle
        elif dx < 0 and dy > 0:
            angle = math.pi - angle
        elif dx < 0 and dy < 0:
            angle = math.pi + angle
        elif dx > 0 and dy < 0:
            angle = 2*math.pi-angle

    return angle

def rad_to_deg(angle: float):
    return 180*angle/math.pi
