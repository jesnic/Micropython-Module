cd ..
cd Firmware
esptool.py -p COM5 -b 115200 write_flash --flash_size=detect 0 esp8266-20191220-v1.12.bin
pause

