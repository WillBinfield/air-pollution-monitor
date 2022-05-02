

class ParticulateReading:

    def __init__(self, pm_2p5, pm_10):
        self.pm_2p5 = pm_2p5
        self.pm_10 = pm_10


class TemperatureHumidityReading:

    def __init__(self, temperature, humidity):
        self.temperature = temperature
        self.humidity = humidity


class CompositeReading:

    def __init__(self, particulate: ParticulateReading, temp_reading: TemperatureHumidityReading):
        self.pm_2p5 = particulate.pm_2p5
        self.pm_10 = particulate.pm_10
        self.temperature = temp_reading.temperature
        self.humidity = temp_reading.humidity
