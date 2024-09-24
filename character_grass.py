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
    r, cx, cy = 210, 800//2, 600//2
    
    for degree in range(-90, 270, 3):
        theta = math.radians(degree)
        x = r * math.cos(theta) + cx
        y = r * math.sin(theta) + cy
        draw_character(x, y)
        
    
def run_top():
    for x in range(90, 720, 10):
        draw_character(x, 510)

def run_right():
    for y in range(510, 80, -10):
        draw_character(720, y)

def run_bottom1():
    for x in range(400, 80, -10):
        draw_character(x, 90)

def run_bottom2():
    for x in range(710, 390, -10):
        draw_character(x, 90)

def run_left():
    for y in range(90, 520, 10):
        draw_character(90, y)


def run_rectangle():
    run_bottom1()
    run_left()
    run_top()
    run_right()
    run_bottom2()  

def run_fir():
    y = 90
    for x in range(400, 720, 10):
        y += 10
        draw_character(x,y)


def run_sec():
    for x in range(710, 80, -10):
        draw_character(x, 400)


def run_thr():
    y = 400
    for x in range(90, 410, 10):
        y -= 10
        draw_character(x,y)


def run_triangle():
    run_fir()
    run_sec()
    run_thr()

while True:
    run_circle()
    run_rectangle()
    run_triangle()
    

close_canvas()
