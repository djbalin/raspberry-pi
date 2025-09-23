import adafruit_ens160

class Ens160:
    def __init__(self, i2c):
        self.ens160 = adafruit_ens160.ENS160(i2c)
          # Check status
    
    def get_eco2(self):
        eco2 = self.ens160.eCO2
        return eco2

    def get_tvoc(self):
        tvoc = self.ens160.TVOC
        return tvoc

    def get_aqi(self):
        aqi = self.ens160.AQI
        return aqi
   
    def get_status(self):
        status = self.ens160.data_validity
        if status == adafruit_ens160.NORMAL_OP:
            print("ENS160: Normal operation")
        if status == adafruit_ens160.WARM_UP:
            print("ENS160: Warming up")
        if status == adafruit_ens160.START_UP:
            print("ENS160: Initial startup")
        if status == adafruit_ens160.INVALID_OUT:
            print("ENS160: Invalid output")
