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

def read_json (file):

    with open(file) as file:
   
        content = json.load(file)    

        return content
