import machine
import network
import time
import os
import socket
import dht
import gc
import json
import urequests

from create_server import create_server

# Creates the config server, in order to receive data
# Returns the arguments to fields
# ssid - string, example: "Home Network"
# password - string , example: "mypassword"
# webpage - string, example: "<html>This is a webpage!</html>"
# fields - list, example: ["username" , "password"]

class SimpleConfigServer:

    def __init__ (self, ssid, password, webpage, fields):

        self.access_point, self.socket = create_server(ssid , password) # Create config. server

        self.webpage = webpage # Assign the html webpage

        self.fields = fields;
        self.arguments = []

    def listen (self):

        # Listen to config. page
        try:
         
            connection, address = self.socket.accept() # Socket accepts any pending connections
            request = connection.recv(1024) # Socket is receiving http requests
            request = str(request, 'utf8') # Decode the request
            connection.send(self.webpage) # Sends the webpage to client
            connection.close() # Closes the connection

            # Check if the request has all fields
            for i in range (len(self.fields)):

                if request.find(self.fields[i]) == -1:

                    raise Exception() # Causes an error on purpouse
         
            request = request.split(" ")
            data = request[1]
            data = data.replace('/?', '')
            data = data.split("&")

            for i in range (len(self.fields)):

                data[i] = data[i].replace(self.fields[i] + "=", '')
                data[i] = data[i].replace("+", ' ')
                data[i] = data[i].replace("%2B", '+')
                self.arguments.append(data[i])

            self.close()
            return self.arguments

        except Exception as exception:

            # In case something goes wrong... So the code won't crash
            print(exception)
            return self.arguments
            time.sleep_ms(500)

    def close(self):

        self.socket.close()
        #del self.accessPoint, self.serverSocket
