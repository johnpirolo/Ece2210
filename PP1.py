'''
pp1.py
Course: ECE 2210 - Python Programming for ECE
Semester: Fall 2025
Name: Jonathan Pirolo
CUID: C93279883
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
    forbidden_ascii = []
    lower = "abcdefghijklmnopqrstuvwxyz"
    upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    digits = "0123456789"
    special = "~`!@#$%^&*()-_+={}[]|\\;:""<>,./?"
    print(f"Password: {pwd}")
    if len(pwd) >= 16 and any(c in lower for c in pwd) and any(c in upper for c in pwd) and any(c in digits for c in pwd) and any(c in special for c in pwd) and not any(" " in c for c in pwd):
        return True
    else:
        return False
   


################# Your input ends here. Do NOT change the following code!!!######################
if __name__ == '__main__':
    while True:
        line = input()
        if line == 'End':
            break
        else:
            print(verify_password(line))
