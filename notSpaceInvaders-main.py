# Imports go at the top
from microbit import *
from random import *
from time import *
import speech
again = True
running = True
player = 2
drop = 0
a = 0
b = 0
p = 0
move = 0
delay = 1000
press = False
is_dodged = True
display.set_pixel(player, 4, 7)
while running:
    b += 1
    x = accelerometer.get_x()
    y = accelerometer.get_y()
    if button_a.was_pressed():
        if player != 0:
            player -= 1
            a = 1
            press = True
    if button_b.was_pressed():
        if player != 4:
            player += 1
            a = -1
            press = True
    if press:
        display.set_pixel(player, 4, 7)
        display.set_pixel(player + a, 4, 0)    
    if is_dodged == True:
        drop = randint(0, 4)
        is_dodged = False
        p += 1
        delay -= 20
        if delay <= 0:
            delay = 1
    display.set_pixel(drop, move, 9)
    if b % delay == 0:
        if move in [0, 1, 2, 3]:
            display.set_pixel(drop, move, 0)
            move += 1
        elif move == 4: 
            if drop == player:
                running = False
            else:
                is_dodged = True
                display.set_pixel(drop, move, 0)
                move = 0
        else:
            move += 1
bri = 9
for i in range(14):
    for j in range(5):
        for h in range(10):
            try:
                display.set_pixel(j, i - h, bri - h)
            except:
                continue        
    sleep(0.05)
display.scroll(p - 1, delay = 300)
if p-1 != 1:
    speech.say("you achieved a score of {} points".format(p-1))
else:
    speech.say("you achieved a score of {} point".format(p-1))