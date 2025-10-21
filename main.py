import sys
import time
import csv
import os
from datetime import datetime

from pi import RaspberryPi
from utils.network import send_sensor_data
from utils.logging import LOG



# LED pins
GREEN_PIN = 17  # row 35 LED anode wire
YELLOW_PIN = 27  # row 40 LED anode wire
RED_PIN = 22  # row 45 LED anode wire



# CSV setup
output_dir = './output'
csv_path = output_dir + '/' + 'sensor_data.csv'
csv_headers = ['timestamp', 'eCO2_ppm', 'TVOC_ppb', 'air_quality_index', 'pressure_hPa', 'temperature_bmp_C', 'humidity_percent']


if not "--no-csv" in sys.argv:
    # Create output directory if it doesn't exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
        LOG(f"[Created output directory: {output_dir}]")


    # Create CSV file with headers if it doesn't exist
    if not os.path.exists(output_dir+"/"+csv_path):
        with open(csv_path, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(csv_headers)
        LOG(f"[Created CSV file: {csv_path}]")

SLEEP_TIME_S = 5*60

try:
    print(f"{datetime.now()}: Initializing measurements...")
    pi = RaspberryPi()

    while True:
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        


        aqi, eco2, tvoc, humidity, pressure, temp = pi.get_readings()

        
        if "--debug" in sys.argv:
            print(timestamp)
            print(f"eCO2: {eco2} ppm (TVOC: {tvoc} ppb)")
            print(f"Air Quality Index: {aqi}")
            print(f"Pressure: {pressure:.2f} hPa")
            print(f"Temperature: {temp:.2f} (BMP) °C")
            print(f"Humidity: {humidity:.2f} %")
            print("-" * 40)
            SLEEP_TIME_S = 5
        else:
            send_sensor_data(tvoc,eco2,temp,aqi,pressure,humidity) 



        if not "--no-csv" in sys.argv:
            # Save to CSV
            with open(csv_path, 'a', newline='') as file:
                writer = csv.writer(file)
                writer.writerow([timestamp, eco2, tvoc, aqi, pressure, temp, humidity])
            print(f"{timestamp}: Data logged to CSV")
        

        time.sleep(SLEEP_TIME_S)

        
except KeyboardInterrupt:
    print("Logging stopped")




