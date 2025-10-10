import adafruit_bmp280

class BMP280:
    def __init__(self, i2c):
        bmp280 = adafruit_bmp280.Adafruit_BMP280_I2C(i2c,address=0x76)
        self.bmp280 = bmp280
    
    def get_pressure(self):
        try:
            pressure = self.bmp280.pressure
            return pressure
        except Exception as e:
            print(f"BMP280 error getting pressure: {e}")
            return None

    def get_temp(self):
        try:
            temp_bmp = self.bmp280.temperature
            return temp_bmp
        except Exception as e:
            print(f"BMP280 error getting temperature: {e}")
            return None

        
