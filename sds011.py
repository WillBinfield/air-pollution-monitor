
from sds011 import *
import time
import Adafruit_DHT

DHT_SENSOR = Adafruit_DHT.DHT22
DHT_PIN = 4

def get_data(n):
    X = 1
    while X < 10:
        sensor.sleep(sleep=False)
        pmt_2_5 = 0
        pmt_10 = 0
        time.sleep(10)
        for i in range(n):
            humidity, temperature = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)
            x = sensor.query()
            pmt_2_5 = x[0]
            pmt_10 = x[1]
            time.sleep(5)
            pmt_2_5 = round(pmt_2_5, 1)
            pmt_10 = round(pmt_10, 1)
            print(f"pm2.5: {pmt_2_5} pm10: {pmt_10} Temp={temperature:0.1f}C Humidity={humidity:0.1f}%")
        sensor.sleep(sleep=True)
        time.sleep(200)
        X += 1
    return pmt_2_5, pmt_10

sensor = SDS011("/dev/ttyUSB0")

pm2, pm10 = get_data(6)

