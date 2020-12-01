'''
Project Name: Turtle Patterns
Author: Peyton Sneddon
Due Date: 10/03/2020
Course: CS1400-003

Ideal height and width are 600 x 800

In this project I learned about how useful functions and loops are.
I also learned how to put in different perameters for the shapes,
that way I could make the shapes different sizes and colors.
'''


from turtle import *

# Atomic shapes:
def draw_triangle(border_color, fill_color, f, l):
    color(border_color, fill_color)
    begin_fill()
    down()
    for _ in range(0, 3):
        forward(f)
        left(l)
    end_fill()
    up()
    
    
def draw_square(border_color, fill_color, h):
    draw_rectangle(border_color, fill_color, h, h)
   
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

def draw_window():
    window_border = 'black'
    window_color = 'white'
    draw_square (window_border, window_color, 20)
    right(90)
    draw_square(window_border, window_color, 20)
    #draw_square(x, 20, 90)
    right(90)
    draw_square(window_border, window_color, 20)
    #draw_square(x, 20, 90)
    right(90)
    draw_square(window_border, window_color, 20)
    
def main():
    '''
    Program starts here.
    '''
    try:
        print("Ideal height and width are 600 x 800")
        width = int(input("Enter screen height "))
        height = int(input("Enter screen length "))
        
            
            
    except ValueError:
        print("Enter postive integers for width and height.")
        return
    
    if width < 1 or height < 1:
        print("Enter postive integers for width and height.")
        return 
    
    # (2) replace pass with your code
    x_orig = -100
    y_orig = -250
    #print(position())
    setup(height,width)
    bgcolor('#00FFFF')
    #speed(0)
    #tracer(False)
   #draw building
    up()
    goto(x_orig, y_orig)
    draw_square('black', 'blue', 200)

    #draw roof
    up()
    left(90)
    forward(200)
    down()
    right(90)
    draw_triangle('black', 'gray', 200, 120)

    #draw first window
    up()
    right(90)
    forward(50)
    left(90)
    forward(40)
    draw_window()

    #draw second window
    up()
    right(90)
    forward(120)
    draw_window()

    #draw door
    up()
    goto(x_orig,y_orig)
    right(90)
    forward(80)
    draw_rectangle('black', 'gray', 40, 80)

    #draw door handle
    left(90)
    forward(40)
    right(90)
    forward(28)
    draw_hex('black', 'red', 5)

    #draw sun
    goto(x_orig,y_orig)
    forward(350)
    left(90)
    forward(350)
    draw_hex('orange', 'orange', 40)
    
    for _ in range (0,6):
        draw_triangle('red', 'yellow', 40, 120)
        forward(40)
        right(60)











    

    



    
if __name__ == "__main__":
    main()
    
