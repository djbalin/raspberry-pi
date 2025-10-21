

import time

from led import LED

GREEN_PIN = 17
YELLOW_PIN = 27
RED_PIN = 22

try:
    print("Initializing test")
    green_led = LED(GREEN_PIN)
    yellow_led = LED(YELLOW_PIN)
    red_led = LED(RED_PIN)
    print("leds initialized")
    while True:
        green_led.on()
        time.sleep(0.2)
        yellow_led.on()
        time.sleep(0.2)
        red_led.on()
        time.sleep(1)
        green_led.off()
        time.sleep(1)
        yellow_led.off()
        time.sleep(1)
        red_led.off()
        time.sleep(1)
except KeyboardInterrupt:
    green_led.off()
    yellow_led.off()
    red_led.off()
    print("LED test stopped")
