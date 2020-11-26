import machine
import network
import time
import os
import socket
import dht
import gc
import json
import urequests

# Super simple function, just reads a file in json format
# Returns its content in python directory

def save_json (file, content):

    with open(file, 'w') as file:
        
        json.dump(content, file)
        
    time.sleep_ms(500)
