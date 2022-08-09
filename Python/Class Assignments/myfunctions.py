# Name: Justine Kim     # Date: 4/8/19
# NetID: jk5565         # Section: CSCI-UA.0002-1
# Assignment 6          # Sourcecode


# line functions
def horizontal_line(width):
    for i in range(width):
        print("*",end='')
    print()

def line(shift,height):
    for i in range(height):
        print(" "*(shift)+"*")
    print()

def vertical_lines(height,width):
    for i in range(height):
        print("*"+" "*(width-2)+"*")
    print()

# set of new functions that are comprised of old functions
def number_0(width):
    height = 3
    horizontal_line(width)
    vertical_lines(height,width)
    horizontal_line(width)

def number_1(width):
    line(width-1,5)

def number_2(width):
    horizontal_line(width)
    height = 1
    shift = 4
    line(shift,height)
    horizontal_line(width)
    height = 1
    shift = 0
    line(shift,height)
    horizontal_line(width)

def number_3(width):
    horizontal_line(width)
    height = 1
    shift = 4
    line(shift,height)
    horizontal_line(width)
    height = 1
    shift = 4
    line(shift,height)
    horizontal_line(width)

def number_4(width):
    height = 2
    vertical_lines(height,width)
    horizontal_line(width)
    shift = 4
    height = 2
    line(shift,height)

def number_5(width):
    horizontal_line(width)
    height = 1
    shift = 0
    line(shift,height)
    horizontal_line(width)
    height = 1
    shift = 4
    line(shift,height)
    horizontal_line(width)

def number_6(width):
    horizontal_line(width)
    height = 1
    shift = 0
    line(shift,height)
    horizontal_line(width)
    height = 1
    vertical_lines(height,width)
    horizontal_line(width)

def number_7(width):
    horizontal_line(width)
    shift = 4
    height = 4
    line(shift,height)

def number_8(width):
    horizontal_line(width)
    height = 1
    vertical_lines(height,width)
    horizontal_line(width)
    height = 1
    vertical_lines(height,width)
    horizontal_line(width)

def number_9(width):
    horizontal_line(width)
    height = 1
    vertical_lines(height,width)
    horizontal_line(width)
    shift = 4
    height = 2
    line(shift,height)

# math operation display functions
def plus(width):
    shift = width - 3
    height = width - 3
    line(shift,height)
    for i in range(width):
        print("*",end='')
    print()
    shift = width - 3
    height = width - 3
    line(shift,height)
    print()
    print()

def minus(width):
    for i in range(width):
        print("*",end='')
    print()
    print()

# check answer function 
def check_answer(number1, number2, answer, operator):
    if operator == "+":
        the_sum = number1 + number2
        return the_sum == answer 
    elif operator == "-":
        difference = number1 - number2
        return difference == answer 
