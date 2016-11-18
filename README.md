# ArduinoTelescopeDustCover
An open source project to automate some aspects of amateur astronomy.

**Aim: Use an Arduino Nano to open and close the dust cover on a telescope.**

Requirements:
- Arduino Nano (like [this](https://www.aliexpress.com/item/Nano-3-0-controller-compatible-with-arduino-nano-CH340-USB-driver-with-CABLE-NANO-V3-0/32478082112.html?spm=2114.01010208.3.11.omwhu1&ws_ab_test=searchweb0_0,searchweb201602_5_10065_10068_10084_10083_10080_10082_10081_10060_10061_10062_10056_10055_10054_10059_10078_10079_10073_10096_10070_10100_10052_423_10050_10051_424,searchweb201603_8&btsid=b7afc5ec-93f1-4158-8d06-f842e11ed59a)
- Servo (like [this](https://www.aliexpress.com/item/Micro-9g-servo-RC-SG90-Aircraft-airplane-model-parts-for-Unique-model-Biplane-Helicopter-Accessories/32677485253.html?spm=2114.01010208.3.21.hMGnOQ&ws_ab_test=searchweb0_0,searchweb201602_5_10065_10068_10084_10083_10080_10082_10081_10060_10061_10062_10056_10055_10054_10059_10078_10079_10073_10096_10070_10100_10052_423_10050_10051_424,searchweb201603_8&btsid=b4745c77-5a61-4155-9d28-949cdfefc80d)
- 2x LED
- 2x 220 Ohm Resistors
- A few wires

Instal Python 2.7.12 (download [here](https://www.python.org/downloads/)

Add python path to PATH (instructions [here](http://stackoverflow.com/questions/3701646/how-to-add-to-the-pythonpath-in-windows-7))

Start a CMD prompt as administrator (instructions [here](https://technet.microsoft.com/en-us/library/cc947813(v=ws.10).aspx)) 

From the CMD prompt we manually install Pip using the following command

`python get-pip.py`

Next we want to install pyserial, again at the CMD prompt we type

`python -m pip install pyserial`

Start the Arduino IDE (download [here](https://www.arduino.cc/en/Main/Software))

Wire up the arduino as follows: 

![alt text][logo]

[logo]: http://i.imgur.com/s5vJ4pn.png "Logo Title Text 2"
