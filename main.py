
import time

from sds011 import SDS011
from Adafruit_DHT import DHT22, read_retry


class ParticulateReading:

    def __init__(self, pm_2_point_5, pm_10):
        self.pm_2_point_5 = pm_2_point_5
        self.pm_10 = pm_10


class TemperatureHumdityReading:

    def __init__(self, temperature, humdity):
        self.temperature = temperature
        self.humidity = humdity


def read_pm_values(sensor: SDS011):
    pm2point5, pm10 = sensor.query()
    return ParticulateReading(pm2point5, pm10)


def read_tmp_hmd_sensor():
    temperature, humidity = read_retry(DHT22, 4)
    return TemperatureHumdityReading(temperature, humidity)


def reading_to_2_decimal_places(particulate_reading: ParticulateReading):
    particulate_reading.pm_2_point_5 = round(particulate_reading.pm_2_point_5, 1)
    particulate_reading.pm_10 = round(particulate_reading.pm_10, 1)


def get_data(n):
    X = 1
    while X < 10:
        sensor.sleep(sleep=False)
        pmt_2_5 = 0
        pmt_10 = 0
        time.sleep(10)
        for i in range(n):
            temperature_humidity_reading = read_tmp_hmd_sensor()
            particulate_reading = read_pm_values()
            reading_to_2_decimal_places(particulate_reading)

            time.sleep(5)

            print(f"pm2.5: {pmt_2_5} "
                  f"pm10: {pmt_10} "
                  f"Temp={temperature_humidity_reading.temperature:0.1f}C "
                  f"Humidity={temperature_humidity_reading.humidity:0.1f}%")

        sensor.sleep(sleep=True)
        time.sleep(200)
        X += 1
    return pmt_2_5, pmt_10

sensor = SDS011("/dev/ttyUSB0")

pm2, pm10 = get_data(6)

