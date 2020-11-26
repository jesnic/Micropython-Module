import serial
import time

# This is a serial console for ESP8266 running micropython
# Don't forget adjusting the port and baudrate for your setup!

port = "COM5"
baudrate = "115200"

ser = serial.Serial(port, baudrate, timeout=0)

# Clear garbage from older sessions
ser.write(b'\r\n')
time.sleep(0.01)
rx = ser.readline().decode()
while rx != ">>> ":

    rx = ser.readline().decode()

    if rx == '':

        ser.write(b'\r\n')
        time.sleep(0.01)
# ----

# Serial loop
while True:
    
    tx = input(rx.replace('\r\n', ''))
    ser.write(tx.encode() + b'\r\n')

    rx = ser.readline().decode()

    # Print loop
    while rx != ">>> " and rx.find('...') == -1:

        if (rx != tx + '\r\n' and rx != ""):
            
            print(rx)

        rx = ser.readline().decode()
        #print(rx)

