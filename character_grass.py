from pico2d import *
import math

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

def draw_character(x, y):
    clear_canvas_now()
    character.draw_now(x, y)
    grass.draw_now(400, 30)
    delay(0.1)

def run_circle():
    print('CIRCLE')

    r, cx, cy = 210, 800//2, 600//2
    
    for degree in range(-90, 270, 3):
        theta = math.radians(degree)
        x = r * math.cos(theta) + cx
        y = r * math.sin(theta) + cy
        draw_character(x, y)
        
    
def run_top():
    print('TOP')
    
    for x in range(90, 720, 10):
        draw_character(x, 510)
    
    pass

def run_right():
    print('RIGHT')

    for y in range(510, 80, -10):
        draw_character(720, y)
    pass

def run_bottom():
    print('BOTTOM')

    for x in range(710, 80, -10):
        draw_character(x, 90)
    
    pass

def run_left():
    print('LEFT')

    for y in range(90, 520, 10):
        draw_character(90, y)


def run_rectangle():
    print('RECTANGLE')

    run_top()
    run_right()
    run_bottom()
    run_left()
    
    pass    

def run_fir():
    print('first')
    y = 90
    for x in range(400, 720, 10):
        y += 10
        draw_character(x,y)

    pass

def run_sec():
    print('second')

    for x in range(710, 80, -10):
        draw_character(x, 400)
    
    pass

def run_thr():
    print('third')
    y = 400
    for x in range(90, 410, 10):
        y -= 10
        draw_character(x,y)
    
    pass

def run_triangle():
    print('TRIANGLE')

    run_fir()
    run_sec()
    run_thr()

    pass

while True:
    run_circle()
    #run_rectangle()
    #run_triangle()
    break
    

close_canvas()
