'''
hw2.py
Course: ECE 2210 - Python Programming for ECE
Semester: Spring 2026
Name: Jonathan Pirolo
CUID: C93279883
Known Bugs: None.
'''
# You CANNOT import other modules
import math

'''
Function I:
Kinematic formula: h = 0.5 * g * t^2  => t = sqrt(2h / g)
Using g = 9.80665 m/s^2 for precision.
'''
def cal_secs_ball_falling1(h):
    g = 9.80665
    t = math.sqrt((2 * h) / g)
    # Requirement: Return integer part only
    return int(t)

'''
Function II:
Calculating time as a float and printing (Void function).
'''
def cal_secs_ball_falling2(h):
    g = 9.80665
    t = math.sqrt((2 * h) / g) 
    # Keep the following print statement as the last statement of this function.
    print(f"It takes {t} seconds for the ball to hit the ground.\n")

'''
Function III:
Formula for altitude h: h = [ (G * M * T^2) / (4 * pi^2) ]^(1/3) - R
Constants:
G = 6.674e-11 (Gravitational constant)
M = 5.97e24   (Mass of Earth in kg)
R = 6.371e6   (Radius of Earth in meters)
'''
def cal_altitude(t_minutes):
    # Convert minutes to seconds
    T = t_minutes * 60
    G = 6.674e-11
    M = 5.97e24
    R = 6.371e6
    pi = math.pi
    
    # Kepler's Third Law rearranged for altitude
    h = ((G * M * T**2) / (4 * pi**2))**(1/3) - R
    return h

'''
Function IV:
Drawing the 2x2 grid using string repetition and concatenation.
'''
def draw_grid():
    # Define the components
    plus = '+'
    minus = ' -' * 4 + ' '
    pipe = '|'
    space = ' ' * 9
    
    # Construct rows
    horizontal_line = (plus + minus) * 2 + plus
    vertical_line = (pipe + space) * 2 + pipe
    
    # Print the grid
    for _ in range(2):
        print(horizontal_line)
        for _ in range(4):
            print(vertical_line)
    print(horizontal_line)

# Function Calls:
# Do NOT modify the code below!!!
print(f'It takes {cal_secs_ball_falling1(100)} seconds for the ball to hit the ground.\n')
cal_secs_ball_falling2(100)
print(cal_secs_ball_falling2(100), '\n')
print(cal_altitude(90), '\n')
print(cal_altitude(45), '\n')
draw_grid()