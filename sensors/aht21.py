import adafruit_ahtx0

class Aht21:
    def __init__(self, i2c):
        self.aht21 = adafruit_ahtx0.AHTx0(i2c)
    
    def get_humidity(self):
        humidity = self.aht21.relative_humidity
        return humidity