from pico2d import *
import math

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

x = 400
y = 90
while(True):
    clear_canvas_now()
    grass.draw_now(400, 30)
    character.draw_now(x, y)
    if(x <= 790):
        x = x + 2
    elif(x == 790 & y <= 600):
        y = y + 2
    elif(y == 600 & x >= 0):
        x = x - 2
    elif(y <= 600 & x == 0):
        y = y - 2
    
    delay(0.01)

close_canvas()
