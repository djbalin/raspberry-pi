from traffic_light import TrafficLight
GREEN_PIN = 17
YELLOW_PIN = 27
RED_PIN = 22

try:
    print("Initializing test")
    traffic_light = TrafficLight(GREEN_PIN, YELLOW_PIN, RED_PIN)
    print("traffic light initialized")
    while True:
        traffic_light.dance()
except KeyboardInterrupt:
    traffic_light.cleanup()
    print("traffic light test stopped")
