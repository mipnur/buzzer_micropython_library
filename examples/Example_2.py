from machine import Pin, PWM
from buzzer_lib import *
import time
time.sleep(0.1)

buz = buzzer(14)

while True:
    buz.tone(do, 3000, 0.2)
    time.sleep(0.5)
    buz.tone(re, 3000, 0.2)
    time.sleep(0.5)
    buz.tone(mi, 3000, 0.2)
    time.sleep(0.5)
    buz.tone(fa, 3000, 0.2)
    time.sleep(0.5)
    buz.tone(sol, 3000, 0.2)
    time.sleep(0.5)
    buz.tone(la, 3000, 0.2)
    time.sleep(0.5)
    buz.tone(si, 3000, 0.2)
    time.sleep(0.5)
    buz.tone(do, 3000, 0.2)
    time.sleep(0.5)
