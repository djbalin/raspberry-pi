from adafruit_ens160 import ENS160

class Ens160:
    def __init__(self, i2c):
        self.ens160 = ENS160(i2c)
    
    def get_eco2(self):
        eco2 = self.ens160.eCO2
        return eco2

    def get_tvoc(self):
        tvoc = self.ens160.TVOC
        return tvoc

    def get_aqi(self):
        aqi = self.ens160.AQI
        return aqi