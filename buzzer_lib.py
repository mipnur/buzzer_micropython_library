from machine import Pin, PWM
import time

do = 262; re = 294 ;mi = 330; fa = 349; sol = 392; la = 440; si = 494
do_= 277; re_= 311 ;fa_= 370; sol_= 415; la_= 466

black = 0.4; white = 0.8; white_p = 1.2

class buzzer:
    def __init__(self, pin):
        self.pin = PWM(pin)
    
    def tone(self, note, duty, duration):
        self.pin.freq(note)
        self.pin.duty_u16(duty)
        time.sleep(duration)
    
    def melody(self, note, duty, duration, dura):
        for n in range(len(note)):
            self.pin.duty_u16(duty)
            self.pin.freq(note[n])
            time.sleep(duration[n])
            self.pin.duty_u16(0)
            time.sleep(dura)
