'''
pp1.py
Course: ECE 2210 - Python Programming for ECE
Semester: Fall 2025
Name: You Know Who (Replace it with your name)
CUID: (Insert your CUID here)
Known Bugs: If your code contains any mistakes, please list them here.
'''
# You CANNOT import other modules
import sys

redirectIOtoFile = True
if (redirectIOtoFile):
# redirect stdin to a file
    sys.stdin = open('input', 'r')

############ Your input starts here. Do NOT change the above code!!!#################

def verify_password(pwd):
    pass # Replace pass with your code


################# Your input ends here. Do NOT change the following code!!!######################
if __name__ == '__main__':
    while True:
        line = input()
        if line == 'End':
            break
        else:
            print(verify_password(line))
