from machine import Pin, PWM
from buzzer_lib import *
import time
time.sleep(0.1)

buz = buzzer(14)

song = [mi, mi, fa, sol, sol_, sol_, la_, sol_, fa, mi, re, do,
mi, mi, fa, sol, sol_, sol_, la_, sol_, fa, mi, re, do,
sol, sol, la, sol, fa, mi, re]

# The duration of the note: black = 0.4 seconds; white = 0.8 seconds; white_p = 1.2 seconds
dur = [black, black, black, black, black, black, black, black, black, black, white, white,
       black, black, black, black, black, black, black, black, black, black, white, white,
       black, black, black, black, black, white, white]

while True:
    buz.melody(song, 3000, dur, 0.1)
    time.sleep(2)
