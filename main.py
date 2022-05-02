from time import sleep

from Adafruit_DHT import DHT22, read_retry
from sds011 import SDS011

from readings import ParticulateReading, TemperatureHumidityReading, CompositeReading


class PollutionSensor:

    def __init__(self):
        self.particulate_sensor = SDS011("/dev/ttyUSB0")
        self.temp_sensor_type = DHT22
        self.temp_pin = 4

    def _temperature_humidity_reading(self):
        return read_retry(self.temp_sensor_type, self.temp_pin)

    def _particulate_reading(self):
        return self.particulate_sensor.query()

    def return_reading(self):
        pm_2p5, pm_10 = self._particulate_reading()
        temperature, humidity = self._temperature_humidity_reading()
        return CompositeReading(ParticulateReading(pm_2p5, pm_10),
                                TemperatureHumidityReading(temperature, humidity)
                                )

    def return_periodic_readings(self, interval_period, iteration_count):
        sensor_readings = []
        while iteration_count > 0:
            sensor_readings.append(self.return_reading())
            sleep(interval_period)
            iteration_count -= 1

        return sensor_readings


if __name__ == '__main__':
    sensor = PollutionSensor()
    readings = sensor.return_periodic_readings(15, 5)

    for reading in readings:
        print(f"""{reading.temperature}\n
        f"{reading.humidity}\n
        f"{reading.pm_2p5}\n
        f"{reading.pm_10}\n
        """)
