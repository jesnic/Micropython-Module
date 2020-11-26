from simple_config_server import SimpleConfigServer as cfgServer
from save_json import save_json as save

import machine
import network
import time
import os
import socket
import dht
import gc
import json
import urequests

    
time.sleep(1)

ssid = "MyConfigServer"
pwd = "12345678"
html = "<html>Hello world!</html>"
fields = ["field1" , "field2", "field3", "field4"]

server = cfgServer(ssid, pwd, html, fields)
print("Server started!")

arguments = []

while len(arguments) < 4:

    arguments = server.listen()

mydict = {fields[0]:arguments[0] , fields[1]:arguments[1] , fields[2]:arguments[2] , fields[3]:arguments[3]}

save("saves.txt", mydict)
print("Succesfully saved!")

    
