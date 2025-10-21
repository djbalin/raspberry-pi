from led.traffic_light import TrafficLight
from sensors.aht21 import Aht21
from sensors.bmp280 import BMP280
from sensors.ens160 import Ens160
import board
import time
import busio

GREEN_PIN = 17
YELLOW_PIN = 27
RED_PIN = 22

class RaspberryPi:
    def __init__(self, warmup_s = 30):
        i2c = busio.I2C(board.SCL, board.SDA)
        self.ens160 = Ens160(i2c)
        self.bmp280 = BMP280(i2c)
        self.aht21 = Aht21(i2c)

        self.traffic_light = TrafficLight(GREEN_PIN, YELLOW_PIN, RED_PIN)
        print(f"raspberry pi: sensors initialized. warming up (sleeping) {warmup_s} seconds...")
        self.traffic_light.dance_duration(60)
        # time.sleep(warmup_s)
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

    
    def show_color(self, color_code):
        self.traffic_light.all_off()
        time.sleep(0.1)
        if color_code == 5:
            self.traffic_light.red_only()
        elif color_code == 4:
            self.traffic_light.red_on()
            self.traffic_light.yellow_on()
        elif color_code == 3:
            self.traffic_light.yellow_only()
        elif color_code == 2:
            self.traffic_light.green_on()
            self.traffic_light.yellow_on()
        elif color_code == 1:
            self.traffic_light.green_only()
    
 

    def get_readings(self):
        aqi = self.get_aqi()
        eco2 = self.get_eco2()
        tvoc = self.get_tvoc()
        humidity = self.get_humidity()
        pressure = self.get_pressure()
        temp = self.get_temp()

        color_code = get_color_code(tvoc, eco2)
        self.show_color(color_code)
        
        return (aqi, eco2, tvoc, humidity, pressure, temp, color_code)
    

def get_color_code(tvoc, eco2):
    if tvoc > 600 or eco2 > 1200:
        return 5
    if tvoc > 400 or eco2 > 1000:
        return 4
    elif tvoc > 300 or eco2 > 800:
        return 3
    elif tvoc > 150 or eco2 > 600:
        return 2
    else:
        return 1
