''' 
hw3.py
Course: ECE 2210 - Python Programming for ECE
Semester: Spring 2026 
Name: You Know Who (Replace it with your name)
CUID: (Insert your CUID here)
Known Bugs: If your code contains any mistakes, please list them here.
'''

# You CANNOT import other modules
import math
import sys

redirectIOtoFile = True

if(redirectIOtoFile):
    # redirect stdin to a file
    #.stdin = open('input', 'r')
    pass

############ Your input starts here. Do NOT change the above code!!! #################


# Problem 1.(a)
# Complete the function below following the requirements given in hw3.pdf.
def rhombus():
    """ Draw a rhombus of h=5.
    """
    draw_rhombus( 5,"*")
    pass # Replace pass with your code


# Problem 1.(b)
# Complete the function below following the requirements given in hw3.pdf
def draw_rhombus(h, s):
    """ Draw a rhombus of height h using symbol s.
    """
    # Counter will be the amount of symbols to display
    # Midpoint will be used to determine if we should be adding or subtracting fro, counter
    counter = 1 
    midpoint = h // 2 
    layer_count = 0 
    while layer_count < h:
        if layer_count >= midpoint:
            print(f"{" " * (layer_count - midpoint)} {s*counter}\t\n")
            layer_count += 1
            counter -= 2
        else:
            print(f"{" " * ((midpoint-layer_count) + 1)}{s*counter}\t\n")
            layer_count += 1
            counter += 2
        

     # Replace pass with your code


# Problem 2.(a)
# Complete the function below following the requirements given in hw3.pdf
def is_triangle(l1, l2, l3):
    """ Check if three lengths can form a triangle.
    """
    if l1 + l2 < l3 or l2 + l3 < l1 or l3 + l1 < l2:
        return False
    return True
     # Replace pass with your code


# Problem 2.(b)
# Complete the function below following the requirements
# given in hw3.pdf
def interative_is_triangle():
    """ Check if user-entered three lengths can form a triangle.
    """
    l1 = input("L1: ")
    l2 = input("L2:")
    l3 = input("L3: ")
    return is_triangle(int(l1), int(l2), int(l3))
     # Replace pass with your code


# Problem 3
# Complete the function below following the requirements given in hw3.pdf
def guess_number(k):
    """ Guess number k in [1, 9999].
    """
    while True: 
        guess = int(input("Guess number k in [1,9999]"))
        if guess == k: 
            print("well guessed")
            break 
        elif guess < 1 or guess > 9999:
            print("Invalid Input")
        
     # Replace pass with your code


# Problem 4
# Complete the function below following the requirements given in hw3.pdf
def estimate_pi():
    k = 0 
    total_sum = 0 
    iterations = 2
    while k < 10:
        numerator = math.factorial(4 * k) * (1103 + 26390 * k)
        denominator = (math.factorial(k)**4) * (396**(4 * k))
        term = numerator / denominator
        total_sum += term 
        k+=1
    multiplier = (2*math.sqrt(2) / 9801)
    one_over_pi = multiplier * total_sum 
    print(one_over_pi)
    print(f"Pi is approximated to be {1/one_over_pi}")
     # Replace pass with your code


# Problem 5.a)
# Complete the function below following the requirements given in hw3.pdf
def check_digit(n):
    n = str(n)
    for i in n:
        if int(i) % 2 != 0:
            print("Odd")
    print("Even")
     # Replace pass with your code


# Problem 5.b)
# Complete the function below following the requirements given in hw3.pdf
def find_odd_digit_numbers(a, b):
    for i in range(a, b):
        check_digit(i)


################# Your input ends here. Do NOT change the following code!!! ######################
if __name__ == '__main__':
    print("P1.(a): The following is the output of rhombus():")
    rhombus()

    print()
    print()
    print("P1.(b): The following is the output of draw_rhombus():")
    draw_rhombus(7, '%')
    draw_rhombus(9, '$')

    print()
    print()
    print("P2.(a): The following is the output of is_triangle():")
    is_triangle(1, 4, 6)
    is_triangle(6, 16, 20)
    is_triangle(6, 6, 6)

    print()
    print()
    print("P2.(b): The following is the output of interactive_is_triangle():")
    interative_is_triangle()
    interative_is_triangle()
    interative_is_triangle()

    print()
    print()
    print("P3: The following is the output of guess_number():")
   # guess_number(56)
    #guess_number(3467)
    #guess_number(1)

    print()
    print()
    print("P4: The return value of estimate_pi() is", estimate_pi())
    
    print()
    print()
    print("P5.(a): The following is the output of guess_number():")
    print(check_digit(447))
    print(check_digit(28282))
    print(check_digit(6003))
    
    print()
    print()
    print("P5.(b): The following is the output of find_odd_digit_numbers(a, b)")
    find_odd_digit_numbers(12, 48304)

