import RPi.GPIO as GPIO
import time

# Use BCM pin numbering
GPIO.setmode(GPIO.BCM)

# Define GPIO pins for LEDs (match your wiring)
GREEN_PIN = 17  # row 35 LED anode wire
YELLOW_PIN = 27  # row 40 LED anode wire
RED_PIN = 22  # row 45 LED anode wire


class LED:
    def __init__(self, pin):
        self.pin = pin
        GPIO.setup(self.pin, GPIO.OUT)

    def on(self):
        GPIO.output(self.pin, GPIO.HIGH)

    def off(self):
        GPIO.output(self.pin, GPIO.LOW)

    def toggle(self):
        GPIO.output(self.pin, GPIO.HIGH if GPIO.input(self.pin) == GPIO.LOW else GPIO.LOW)