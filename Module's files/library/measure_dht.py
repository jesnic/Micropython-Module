import machine
import network
import time
import os
import socket
import dht
import gc
import json
import urequests

class measure:

    def __init__ (self, sensor_pin, reading_time, samples_per_mean=4):

        pin = machine.Pin(sensor_pin)

        self.sensor = dht.DHT11(pin) # Define DHT's pin

        self.lastReading = 0 # Time counter for measurements

        self.values_temperature = []
        self.values_humidity = []
        self.reading_time = reading_time
        self.sampling_time = int(self.reading_time/samples_per_mean)
        self.samples_per_mean = samples_per_mean
        self.mean_temperature = -999
        self.mean_humidity = -999

    def process (self):

        delta_time = time.ticks_diff(time.ticks_ms(), self.lastReading)

        if delta_time >= (self.sampling_time):

            sensor.measure()
            temperature = self.sensor.temperature()
            humidity = self.sensor.humidity()
            self.lastReading = time.ticks_ms()

            if len(values_temperature) < samples_per_mean and len(values_humidity) < samples_per_mean:

                values_temperature.append(temperature)
                values_humidity.append(humidity)

            if len(values_temperature) >= samples_per_mean and len(values_humidity) >= samples_per_mean:

                summTemperature = 0
                summHumidity = 0
                
                for i in range (0, samples_per_mean, 1):
                    
                    summTemperature += values_temperature[i]
                    summHumidity += values_humidity[i]

                mean_temperature = summTemperature / samples_per_mean
                mean_humidity = summHumidity / samples_per_mean
                           
                self.values_temperature = []
                self.values_humidity = []

                return 0, mean_temperature, mean_humidity
            
            #delta_time = 0
            del pin
            return (self.reading_time - self.sampling_time*len(values_temperature)), -999, -999
            
        
