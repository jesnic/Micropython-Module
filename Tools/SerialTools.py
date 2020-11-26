import serial
import time

# This script has some useful serial tools for ESP8266 running micropython

def upload_file(file, path="/"):

    clear_garbage()

    with open(file, 'r') as f:
        
        file = file.split('/')
        code = f.read().replace('\n' , '\\n')
        ser.write( ('f = open("' + path + file[-1] + '" , "w+")\r\n').encode())
        ser.write( ('f.write("' + code + '")\r\n').encode() )
        ser.write(b'f.close()\r\n')

        print('LOADING FILE...')
        ser.flushInput()
        time.sleep(2)

def download_file(file):

    clear_garbage()

    ser.write( ('open("' + file + '", "r").read()\r\n').encode() )

    rx = ser.readline().decode()
    time.sleep(0.2)
    rx = ser.readline().decode()
    time.sleep(0.2)
    rx = ser.readline().decode()
    print(rx)
    rx = rx.replace("\\n", "\\\n")
    rx = rx.replace("\\", "")
    rx = rx[1:len(rx)]
    rx = rx[0:len(rx)-3]

    print('DOWNLOADING FILE...')

    with open(file, 'w+') as f:

        f.write(rx)
    
    ser.flushInput()
    time.sleep(2)

              
def remove_file (file):

    clear_garbage()

    ser.write(b'import os\r\n')
    ser.write( ('os.remove("' + file + '")\r\n').encode() )

    print('REMOVING FILE...')
    time.sleep(2)
    ser.flushInput()
    

def list_directory(path='/'):

    ser.write(b'import os\r\n')
    ser.write( ('os.listdir(' + str('"') + path + str('"') + ')\r\n').encode() )
    
    rx = ser.readline().decode()
    while rx != '>>> ':

        if rx != 'os.listdir(' + path + ')\r\n':
        
            print(rx)

        rx = ser.readline().decode()


def execute_command (command):

    tx = command
    ser.write(tx.encode() + b'\r\n')
 
    rx = ser.readline().decode()
    # Print loop
    while rx != '>>> ':

        if (rx != tx + '\r\n') and rx != "":
            
            print(rx)

        if rx.find('...') != -1:

            break

        rx = ser.readline().decode()
    

def clear_garbage():

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


ser = serial.Serial('COM5', '115200', timeout=0)

clear_garbage()

print('*************************')
print('upload - upload a file to the board')
print('download - download a file from the board')
print('rm - remove file')
print('ls - list directory')
print('exec - execute command')
print('*************************')

while True:

    try:

        print("")
        action = input("Action: ")

        if action.lower() == "upload":

            file = input("Path to file in your pc: ")
            print("Leave the next field blank for root (/)")
            path = input("Path to file in board: ")
            upload_file(file, path)

        if action.lower() == "download":

            file = input("Path to file in board: ")
            download_file(file)

        elif action.lower() == "rm":

            print("Don't forget to add the extension (.py .txt .json)")
            file = input("Path to file in board: ")
            remove_file(file)

        elif action.lower() == "ls":

            path = input("Path: ")
            list_directory(path)

        elif action.lower() == "exec":

            command = input("Command: ")
            execute_command(command)

        else:

            print("Action not found, sorry!")
            print("")
            print('*************************')
            print('load - load/save file')
            print('rm - remove file')
            print('ls - list directory')
            print('exec - execute command')
            print('*************************')
            print("")

    except Exception as exception:

        print("")
        print(exception)
        print("")
        
    
