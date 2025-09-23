import sys
import time
import csv
import os
from datetime import datetime

from pi import RaspberryPi
from utils.network import send_sensor_data
from utils.logging import LOG



SLEEP_TIME_S = 5*60

try:
    print(f"{datetime.now()}: Initializing measurements...")
    pi = RaspberryPi(10)

    while True:
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        


        aqi, eco2, tvoc, humidity, pressure, temp = pi.get_readings()

        

        print(timestamp)
        pi.print_status()
        print(f"eCO2: {eco2} ppm (TVOC: {tvoc} ppb)")
        print(f"Air Quality Index: {aqi}")
        print(f"Pressure: {pressure:.2f} hPa")
        print(f"Temperature: {temp:.2f} (BMP) °C")
        print(f"Humidity: {humidity:.2f} %")
        print("-" * 40)
        SLEEP_TIME_S = 5
     

        time.sleep(SLEEP_TIME_S)

        
except KeyboardInterrupt:
    print("Logging stopped")




