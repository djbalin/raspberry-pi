

import time

from .led import LED


class TrafficLight:
    def __init__(self, green_pin, yellow_pin, red_pin):
        self.green_led = LED(green_pin)
        self.yellow_led = LED(yellow_pin)
        self.red_led = LED(red_pin)

    def green_on(self):
        self.green_led.on()
    def yellow_on(self):
        self.yellow_led.on()
    def red_on(self):
        self.red_led.on()
    def green_off(self):
        self.green_led.off()
    def yellow_off(self):
        self.yellow_led.off()
    def red_off(self):
        self.red_led.off()

    def green_only(self):
        self.green_on()
        self.yellow_off()
        self.red_off()
    def yellow_only(self):
        self.green_off()
        self.yellow_on()
        self.red_off()

    def red_only(self):
        self.green_off()
        self.yellow_off()
        self.red_on()
    
    def all_on(self):
        self.green_on()
        self.yellow_on()
        self.red_on()
    def all_off(self):
        self.green_off()
        self.yellow_off()
        self.red_off()
    
    def cleanup(self):
        self.green_led.cleanup()
        self.yellow_led.cleanup()
        self.red_led.cleanup()
    

    def dance(self):
        self.green_only()
        time.sleep(0.2)
        self.yellow_only()
        time.sleep(0.2)
        self.red_only()
        time.sleep(1)
        self.all_off()
        time.sleep(0.5)
        self.green_on()
        time.sleep(0.1)
        self.yellow_on()
        time.sleep(0.1)
        self.red_on()
        time.sleep(1)
        self.red_off()
        time.sleep(0.05)
        self.yellow_off()
        time.sleep(0.05)
        self.green_off()
        time.sleep(0.05)
        self.all_on()
        time.sleep(1)
        self.all_off()
        time.sleep(0.5)
        self.green_on()
        time.sleep(0.1)
        self.yellow_on()


    def dance_duration(self, duration_s):
        num_dances = duration_s/5
        for i in range(0,5):
            self.dance()
