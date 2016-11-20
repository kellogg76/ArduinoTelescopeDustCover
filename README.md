# ArduinoTelescopeDustCover
An open source project to automate some aspects of amateur astronomy.

**Aim: Use an Arduino Nano to open and close the dust cover on a telescope.**

Requirements:
- Arduino Nano (like [this](https://www.aliexpress.com/item/Nano-3-0-controller-compatible-with-arduino-nano-CH340-USB-driver-with-CABLE-NANO-V3-0/32478082112.html?spm=2114.01010208.3.11.omwhu1&ws_ab_test=searchweb0_0,searchweb201602_5_10065_10068_10084_10083_10080_10082_10081_10060_10061_10062_10056_10055_10054_10059_10078_10079_10073_10096_10070_10100_10052_423_10050_10051_424,searchweb201603_8&btsid=b7afc5ec-93f1-4158-8d06-f842e11ed59a)
- Servo (like [this](https://www.aliexpress.com/item/Micro-9g-servo-RC-SG90-Aircraft-airplane-model-parts-for-Unique-model-Biplane-Helicopter-Accessories/32677485253.html?spm=2114.01010208.3.21.hMGnOQ&ws_ab_test=searchweb0_0,searchweb201602_5_10065_10068_10084_10083_10080_10082_10081_10060_10061_10062_10056_10055_10054_10059_10078_10079_10073_10096_10070_10100_10052_423_10050_10051_424,searchweb201603_8&btsid=b4745c77-5a61-4155-9d28-949cdfefc80d)
- 2x LED
- 2x 220 Ohm Resistors
- A few wires
- Posterboard (Very light weight)

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

[logo]: http://i.imgur.com/s5vJ4pn.png

When a serial connection is opened to an Arduino it resets itself, this is a problem for us as the code won’t work as intended, so to get around this we’ll use a 100uF capacitor between the Reset and Ground. This is a simple non-permanent solution, but it does mean that to upload code to the Arduino we need to either press the reset button on the Nano when we’re uploading or temporarily remove the capacitor when uploading.

Connect the Nano to the computer and make note of the COM port it’s using (in my case i'm using COM9 so we’ll use that in the python code later), this can be found in the Arduino IDE (where?). Upload the Dust_Cover.ide code to the Arduino.

Save the open.py and close.py files onto the host computer that has Python installed, connect the arduino to the host via USB, and then double click the open.py or close.py files. Each will send a command over the serial connection and will light the corresponding LED (White for OPEN, Red for CLOSE). **Once wxGUI.py is working substitute this text.**
Install wxPython from [here](https://www.wxpython.org/download.php). 

Once everything is working we can add the servo and alter the Arduino code.

**Adding the servo**

Instructions are [here](http://playground.arduino.cc/Learning/SingleServoExample), but all we're doing is:

1. Connect the red from the servo to +5V on Arduino.

2. Connect black/brown from the servo to Gnd on Arduino.

3. Connect white/orange from the servo to Analog 0 on Arduino.

Now we modify the Arduino code to include the servo. The arduino file is called Dust_Cover_Servo.ide, upload it to the Arduino and change the values for `static int open_angle` and `static int open_angle` to suit your configuration.

Affix the servo to the OTA.

**Controlling a Flat Box**
To control my flat box (from Ali) I bought a 4 relay switch (from Ali) and wired it up to be in a Normally Open (NO) format so that when theres no signal from the Arduino the relay is not activating the flat panel.

The Arduino code for this step is called Elentirmo_v0.1.ide, upload it to the Arduino and wire digital Pin 10 on the Arduino to CH1 on Relay Module as below. **Fritz**

I've also created a Python GUI to control the Dust Cover and Flat Box, it's called Elentirmo_GUI_v0.1.py. Make sure you've installed Pyserial before running it. You also need to change the COM to whichever COM your Arduino is using.

**pics of GUI**

**Future Expansion:**
- How to make sure device is always COM9
- Add capability to switch on/off the flat frame box with a relay
- Add capability to monitor temperature/humidity and also rainfall
- Add capability to open/close the roof
- Improve the wxGUI to include current state of dust cover/roof/flat frame box, jog buttons for open/close, show temp/humidity.
