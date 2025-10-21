

import time

from led import LED
from led import TrafficLight
GREEN_PIN = 17
YELLOW_PIN = 27
RED_PIN = 22

try:
    print("Initializing test")
    traffic_light = TrafficLight(LED(GREEN_PIN), LED(YELLOW_PIN), LED(RED_PIN))
    print("traffic light initialized")
    while True:
        traffic_light.dance()
except KeyboardInterrupt:
    traffic_light.cleanup()
    print("traffic light test stopped")
