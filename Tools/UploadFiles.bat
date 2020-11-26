cd ..
cd Module's files
ampy -p COM4 ls
ampy -p COM4 rmdir /
timeout /t 2
ampy -p COM4 put config.txt
timeout /t 2
ampy -p COM4 put boot.py
timeout /t 2
ampy -p COM4 put main.py
timeout /t 2
ampy -p COM4 put library.py
timeout /t 2
ampy -p COM4 put configMode.py
timeout /t 2
ampy -p COM4 put offlineMode.py
timeout /t 2
ampy -p COM4 put onlineMode.py
timeout /t 2
ampy -p COM4 ls
pause
