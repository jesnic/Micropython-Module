
# Creates a server with a given ssid and password
# Returns the acessPoint and serverSocket (used to manage connections)
# ssid - string
# password - string (min. 8 characters)

def create_server (ssid, password):

    import network
    import socket
    import time

    access_point = network.WLAN(network.AP_IF) # Sets the WLAN to AP_IF (Acess Point mode)
    access_point.active(True)
    access_point.config(essid=ssid, password=password) # Configure the network
    time.sleep_ms(2000)
    
    address = socket.getaddrinfo('192.168.4.1', 80)[0][-1] # Returns ('192.168.4.1, 80')
    
    socket = socket.socket() # Creates the socket
    socket.bind(address) # Connects socket to 192.168.4.1:80
    socket.listen(1) # Now socket is listening 

    return access_point, socket
