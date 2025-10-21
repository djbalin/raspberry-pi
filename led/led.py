import RPi.GPIO as GPIO
import time

# Use BCM pin numbering
GPIO.setmode(GPIO.BCM)

class LED:
    def __init__(self, pin):
        self.pin = pin
        GPIO.setup(self.pin, GPIO.OUT)

    def on(self):
        GPIO.output(self.pin, GPIO.HIGH)
        print(self.pin)

    def off(self):
        GPIO.output(self.pin, GPIO.LOW)
        print(self.pin)

    def toggle(self):
        GPIO.output(self.pin, GPIO.HIGH if GPIO.input(self.pin) == GPIO.LOW else GPIO.LOW)
    
    def cleanup(self):
        self.off()
        GPIO.cleanup(self.pin)
