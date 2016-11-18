# ArduinoTelescopeDustCover
An open source project to automate some aspects of amateur astronomy.

**Aim: Use an Arduino Nano to open and close the dust cover on a telescope.**

Requirements:
-Arduino Nano
-Servo
-2x LED
-2x 220 Ohm Resistors
-A few wires

Installed Python 2.7.12 (download [here](https://www.python.org/downloads/)

Add python path to PATH (instructions [here](http://stackoverflow.com/questions/3701646/how-to-add-to-the-pythonpath-in-windows-7))

Start a CMD prompt as administrator (instructions [here](https://technet.microsoft.com/en-us/library/cc947813(v=ws.10).aspx)) 

From the CMD prompt we manually install Pip using the following command
$python get-pip.py
Next we want to install pyserial, again at the CMD prompt we type
$python -m pip install pyserial


Start the Arduino IDE (download here)
Wire up the arduino as follows
