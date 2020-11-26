import machine
import network
import time
import os
import socket
import dht
import gc
import json
import urequests

# Connects to a specific network
# Returns the station
# ssid - string
# password - string

def connect (ssid, password):

    station = network.WLAN(network.STA_IF)
    station.active(True)
    station.connect(ssid, password)
    time.sleep(10)

    return station
