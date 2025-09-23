from sensors.aht21 import Aht21
from sensors.bmp280 import BMP280
from sensors.ens160 import Ens160
import board
import time
import busio

class RaspberryPi:
    def __init__(self, warmup_s = 60):
        i2c = busio.I2C(board.SCL, board.SDA)
        self.ens160 = Ens160(i2c)
        self.bmp280 = BMP280(i2c)
        self.aht21 = Aht21(i2c)
        print(f"raspberry pi: sensors initialized. warming up (sleeping) {warmup_s} seconds...")
        time.sleep(warmup_s)
        print("raspberry pi: warmup complete")
    
    def get_aqi(self):
        return self.ens160.get_aqi()
    
    def get_eco2(self):
        return self.ens160.get_eco2()

    def get_tvoc(self):
        return self.ens160.get_tvoc()

    def get_humidity(self):
        return self.aht21.get_humidity()

    def get_pressure(self):
          return self.bmp280.get_pressure()

    def get_temp(self):
        return self.bmp280.get_temp()

    def print_status(self):
        return self.ens160.get_status()

    def get_readings(self):
        aqi = self.get_aqi()
        eco2 = self.get_eco2()
        tvoc = self.get_tvoc()
        humidity = self.get_humidity()
        pressure = self.get_pressure()
        temp = self.get_temp()
        
        return (aqi, eco2, tvoc, humidity, pressure, temp)
    
