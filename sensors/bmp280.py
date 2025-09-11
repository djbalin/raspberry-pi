import adafruit_bmp280

class BMP280:
    def __init__(self, i2c):
        bmp280 = adafruit_bmp280.Adafruit_BMP280_I2C(i2c,address=0x76)
        self.bmp280 = bmp280
    
    def get_pressure(self):
          pressure = self.bmp280.pressure
          return pressure

    def get_temp(self):
        temp_bmp = self.bmp280.temperature
        return temp_bmp

        
