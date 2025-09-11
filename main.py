import sys
import time
import csv
import os
from datetime import datetime

from pi import RaspberryPi
from utils.network import send_sensor_data




# CSV setup
csv_filename = 'sensor_data.csv'
csv_headers = ['timestamp', 'eCO2_ppm', 'TVOC_ppb', 'air_quality_index', 'pressure_hPa', 'temperature_bmp_C', 'humidity_percent']




# Create CSV file with headers if it doesn't exist
if not os.path.exists(csv_filename):
    with open(csv_filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(csv_headers)

try:
    print("Initializing measurements...")
    while True:
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        

        pi = RaspberryPi()

        aqi, eco2, tvoc, humidity, pressure, temp = pi.get_readings()
        
        if "--debug" in sys.argv:
            print(timestamp)
            print(f"eCO2: {eco2} ppm (TVOC: {tvoc} ppb)")
            print(f"Air Quality Index: {aqi}")
            print(f"Pressure: {pressure:.2f} hPa")
            print(f"Temperature: {temp:.2f} (BMP) °C")
            print(f"Humidity: {humidity:.2f} %")
            print("-" * 40)
        else:
            send_sensor_data(tvoc,eco2,temp,aqi,pressure,humidity) 





        if "--save-csv" in sys.argv:
            # Save to CSV
            with open(csv_filename, 'a', newline='') as file:
                writer = csv.writer(file)
                writer.writerow([timestamp, eco2, tvoc, aqi, pressure, temp, humidity])
            print(f"{timestamp}: Data logged to CSV")
        
        time.sleep(10*60)  # 10 minutes

        
except KeyboardInterrupt:
    print("Logging stopped")




