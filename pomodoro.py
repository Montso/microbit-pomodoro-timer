from microbit import *
from utime import sleep

whirl_pool = [(2, 2), (3, 2), (3, 3), (2, 3), (1, 3), (1, 2), (1, 1), (2, 1), (3, 1), (4, 1), (4, 2), (4, 3), (4, 4), (3, 4), (2, 4), (1, 4), (0,4), (0, 3), (0, 3), (0, 2), (0, 1), (0, 0), (1, 0), (2, 0), (3, 0), (4, 0)]

reverse_whirl_pool = [(4, 0), (3, 0), (2, 0), (1, 0), (0, 0), (0, 1), (0, 2), (0, 3), (0, 3), (0, 4), (1, 4), (2, 4), (3, 4), (4, 4), (4, 3), (4, 2), (4, 1), (3, 1), (2, 1), (1, 1), (1, 2), (1, 3), (2, 3), (3, 3), (3, 2), (2, 2)]

falling_towers = [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (1, 0), (1, 1), (1, 2), (1, 3), (1, 4), (2, 0), (2, 1), (2, 2), (2, 3), (2, 4), (3, 0), (3, 1), (3, 2), (3, 3), (3, 4), (4, 0), (4, 1), (4, 2), (4, 3), (4, 4)]

domino = [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (1, 4), (1, 3), (1, 2), (1, 1), (1, 0), (2, 0), (2, 1), (2, 2), (2, 3), (2, 4), (3, 4), (3, 3), (3, 2), (3, 1), (3, 0), (4, 0), (4, 1), (4, 2), (4, 3), (4,4)]

all_on = Image('99999:'
               '99999:'
               '99999:'
               '99999:'
               '99999:'
               '99999')
led_init = 1

def countdown(style=falling_towers):
    if led_init == 1:
        display.show(all_on)
        toggle = 0 #toggle LEDs to 0 - off
    else:
        display.clear()
        toggle = 9 #toggle LEDS to 9 - brightest

    for led in range(25):
        sleep(60)
        display.set_pixel(style[led][0], style[led][1], toggle)
    display.scroll('Time to break', delay=150, wait=True)

def rest_countdown(style=falling_towers):
    if led_init == 1:
        display.show(all_on)
        toggle = 0
    else:
        display.clear()
        toggle = 9

    for led in range(25):
        sleep(12)
        display.set_pixel(style[led][0], style[led][1], toggle)
    display.scroll('Break out', delay=150, wait=True)

while True:
    if button_a.is_pressed():
        countdown(falling_towers)
    elif button_b.is_pressed():
        rest_countdown(whirl_pool)