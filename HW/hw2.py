'''
hw2.py
Course: ECE 2210 - Python Programming for ECE
Semester: Spring 2026
Name: Jonathan Pirolo
CUID: C93279883
Known Bugs: If your code contains any mistakes, please list them here.
'''
# You CANNOT import other modules
import math
'''
Function I:
Complete the following function called "cal_secs_ball_falling1".
A ball is dropped from a tower of height h (in meters) with initial velocity zero.
Function "cal_secs_ball_falling1" takes the height of the tower as input and
RETURNS the time (in seconds) the ball takes until it hits the ground (ignoring air
resistance).
Refer to hw2.pdf for the kinematic formula.
Requirement(s):
1) The return value is an integer that only keeps the integer part of the
computed result.
'''
def cal_secs_ball_falling1(h):
    seconds = (2*h)/9.8
    return seconds

'''














Function II:
Complete the following function called "cal_secs_ball_falling2":
A ball is AGAIN dropped from a tower of height h (in meters) with initial velocity
zero.
Function "cal_secs_ball_falling2" takes the height of the tower as input and
CALCULATES AND PRINTS the time (in seconds) the ball takes until it hits the
ground, ignoring air resistance.
Requirement(s):
1) The displayed time is a floating-point number (i.e., no rounding needed).
2) Function "cal_secs_ball_falling2" is a VOID function.
'''
def cal_secs_ball_falling2(h):
    t = 0 # t is the number of secs the ball takes until hitting the ground
# Insert your code of calculating t here.
# Keep the following print statement as the last statement of this function.
    seconds = (2*h)/9.8
    t = seconds
    print(f"It takes {t} seconds for the ball to hit the ground.\n")
'''
Function III:
Complete the following function called "cal_altitude" that
calculates and returns the needed altitude h (in meters) above the earth’s surface
that
the satellite must have so that it orbits the planet once every t minutes.
Refer to hw3.docx for the formula used to calculate the altitude.
Hint: The parameter t is in minutes and T in the given formula is in seconds!
'''
def cal_altitude(t):
    pass # Replace pass with your code
'''
Function IV:
Complete the following function called "darw_grid" that draws a grid
like the one shown in "hw3.pdf", which is only composed of ‘+’, ‘-’, ‘|’ and ‘ ’
(space).
Hint: Consider using string addition (concatenation) and multiplication
(repetition).
'''
def draw_grid():
    pass # Replace pass with your code
# Function Calls:
# Do NOT modify the code below!!!
    print(f'It takes {cal_secs_ball_falling1(100)} seconds for the ball to hit theground.\n')
    cal_secs_ball_falling2(100)
    print(cal_secs_ball_falling2(100), '\n')
    print(cal_altitude(90), '\n')
    print(cal_altitude(45), '\n')
draw_grid()
