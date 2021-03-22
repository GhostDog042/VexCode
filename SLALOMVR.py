# ------------------------------------------
# 
# 	Project:      VEXcode Project
#	Author:       VEX
#	Created:
#	Description:  VEXcode VR Python Project
# 
# ------------------------------------------

# Library imports
from vexcode import *

# Add project code in "main"
F = "F"
R = "R"
P = "P"
S = "S"
drivetrain.set_drive_velocity(100, PERCENT)
drivetrain.set_turn_velocity(100, PERCENT)


def zewm(drec, tur, mod = 2, dist = 70):
    if drec == "F":
        drivetrain.drive_for(FORWARD, dist*mod, MM)
    elif drec == "R":
        drivetrain.drive_for(REVERSE, dist*mod, MM)
    else:
        brain.print("INVALID DIRECTION. WILL ONLY EXCEPT 'F' OR 'R' DUMBASS.")
    if tur == "P":
        drivetrain.turn_for(LEFT, 90, DEGREES)
    elif tur == "S":
        drivetrain.turn_for(RIGHT, 90, DEGREES)
    else:
        brain.print("INVALID DIRECTION. WILL ONLY EXCEPT 'P' OR 'S' DUMBASS.")
"""
STOP EATING MY SPACE ELSE
"""
def main():
    drivetrain.drive_for(FORWARD, 900, MM)
    drivetrain.turn_for(RIGHT, 90, DEGREES)
    drivetrain.drive_for(FORWARD, 900, MM)
    drivetrain.turn_for(RIGHT, 90, DEGREES)
    pen.move(DOWN)
    drivetrain.drive_for(FORWARD, 50, MM)
    drivetrain.turn_for(LEFT, 90 + 45, DEGREES)
    zewm(F,S)
    zewm(F,P)
    zewm(F,S)
    zewm(F,P,1)
    
    zewm(R,S,1)
    zewm(R,P)
    zewm(R,S)
    zewm(R,P)
    zewm(R,S)
    zewm(R,P)
    zewm(R,S,1)
    
# VR threads — Do not delete
vr_thread(main())
