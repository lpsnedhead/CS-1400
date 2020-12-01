'''
Project Name: Turtle Patterns 2
Author: Peyton Sneddon
Due Date: 10/03/2020
Course: CS1400-003



In this project I learned about how useful functions and loops are.
I also learned how to put in different perameters for the shapes,
that way I could make the shapes different sizes and colors.
'''

from turtle import *
from sys import *

# Atomic shapes:
  
def draw_triangle(border_color, fill_color, f, l):
    lesser_angles = l
    #greater_angle = (360 - (lesser_angles * 2))
    color(border_color, fill_color)
    begin_fill()
    down()
    for _ in range(0, 3):
        forward(f)
        left(lesser_angles)
    end_fill()
    up()
    
def draw_square(border_color, fill_color, h):
    color(border_color, fill_color)
    begin_fill()
    down()
    for _ in range(0,4):
        forward(h)
        left(90)
    end_fill()    
    up()
'''    
def draw_square(border_color, fill_color, h):
    draw_rectangle(border_color, fill_color, h, h)
'''   
def draw_rectangle(border_color, fill_color, w, h):
    color(border_color, fill_color)
    begin_fill()
    down()
    for _ in range(0, 2):
        forward(w)
        left(90)
        forward(h)
        left(90)
    end_fill()
    
    up()
    
def draw_hex(border_color, fill_color, h):
    color(border_color, fill_color)
    begin_fill()
    down()
    for _ in range(0,6):
        forward(h)
        right(60)
    end_fill()
    up()      

def draw_window(size):
    window_border = 'black'
    window_color = 'white'
    draw_square (window_border, window_color, (size * .1))
    right(90)
    draw_square(window_border, window_color, (size * .1))
    #draw_square(x, 20, 90)
    right(90)
    draw_square(window_border, window_color, (size * .1))
    #draw_square(x, 20, 90)
    right(90)
    draw_square(window_border, window_color, (size * .1))

# Multi-shapped drawings
def draw_house(x_orig, y_orig, proportion):
    size = int(100 * proportion)
    
    #draw building
    up()
    goto(x_orig, y_orig)
    draw_square('black', 'blue', size)

    #draw roof
    goto(x_orig, y_orig)
    speed(2)
    #tracer(True)
    
    up()
    left(90)
    forward(size)
    down()
    right(90)
    draw_triangle('black', 'gray', size, 120)

    '''
    Draw Windows
    '''
    #draw first window
    
    goto(x_orig, y_orig)
    up()
    left(90)
    forward(size - (size / 4))
    right(90)
    forward(size * .2)
    draw_window(size)

    #draw second window
    up()
    right(90)
    forward(size * .6)
    draw_window(size)

    #draw door
    
    up()
    goto(x_orig,y_orig)
    right(90)
    forward(size * .4)
    draw_rectangle('black', 'gray', (size * .2), (size * .4))

    #draw door handle
    #tracer(True)
    goto(x_orig,y_orig)
    left(90)
    forward(size * .2)
    right(90)
    forward(size * .55)
    draw_hex('black', 'red', (size * .025))

def draw_sun(x_orig, y_orig,proportion):
    size = int(100 * proportion)
    goto(x_orig,y_orig)
    forward(size * 3.5)
    left(90)
    forward(size * 3.5)
    draw_hex('orange', 'orange', (size * .4))
        #draw reys of sun
    for _ in range (0,6):
        draw_triangle('red', 'yellow', (size * .4), 120)
        forward((size * .4))
        right(60)
        
def draw_moon(x_orig, y_orig,proportion):
    size = int(100 * proportion)
    goto(x_orig,y_orig)
    forward(size * 3.5)
    left(90)
    forward(size * 3.5)
    draw_hex('grey', 'white', (size * .4))    
    forward(size * .15)
    right(90)
    forward(size * .15)
    draw_hex('grey', 'grey', (size * .1))
    forward(size * .15)
    left(45)
    forward(size * .15)
    draw_hex('grey', 'grey', (size * .1))
    left(135)
    forward(size * .15)
    draw_hex('grey', 'grey', (size * .1))

def main():

    try:
        '''
        if len(argv) != 4:
            raise ValueError
        height = int(argv[1])         
        width = int(argv[2])
        scene = int(argv[3])
        '''
        height = 800
        width = 800
        scene = 1
        
        print(f"Arguments: {height},{width},{scene}")
    
        if width < 1 or height < 1:
            print("Enter postive integers for width and height.")
            raise ValueError
        if scene != 1 and scene != 2:
            raise ValueError
        
    except ValueError:
        print("Incorrect arguments or argument type! Please enter [file name], [height], [width], scene [1|2]")
        return
    
    picture = 1
    if picture == 1:
            
        #Draw night picture
        bgcolor('black')
        speed(1)
        tracer(False)
        
        #draw houses
        draw_house(-250,-250, 2)
        
        #draw moon
        draw_moon(-125, -250, 1)
            
        #draw mini picture:
        #draw box
        right(180)
        goto(80,-250)
        draw_square('white', '#00FFFF', 120)
        
        #draw house and sun
        draw_house(100,-250, .30)
        draw_sun(100, -250, .19)
        
    # daytime picture:
    if picture == 0:
        
        #Draw night picture
        bgcolor('#00FFFF')
        speed(1)
        tracer(False)
        
        #draw house
        draw_house(-250,-250, 2)
        
        #draw moon
        #tracer(True)
        draw_sun(-125, -250, 1)
            
        #draw mini picture:
        #draw box
        right(90)
        goto(80,-250)
        draw_square('black', 'black', 120)
        
        #draw house and sun
        draw_house(100,-250, .30)
        draw_moon(100, -250, .19)
    
    print("foo")








    

    



    
if __name__ == "__main__":
    main()
    

