# ArduinoTelescopeDustCover
An open source project to automate some aspects of amateur astronomy.

**Aim: Use an Arduino Nano to open and close the dust cover on a telescope and also control and LED lightbox.**

Requirements:
- Arduino Nano (like [this](https://www.aliexpress.com/item/Nano-3-0-controller-compatible-with-arduino-nano-CH340-USB-driver-with-CABLE-NANO-V3-0/32478082112.html?spm=2114.01010208.3.11.omwhu1&ws_ab_test=searchweb0_0,searchweb201602_5_10065_10068_10084_10083_10080_10082_10081_10060_10061_10062_10056_10055_10054_10059_10078_10079_10073_10096_10070_10100_10052_423_10050_10051_424,searchweb201603_8&btsid=b7afc5ec-93f1-4158-8d06-f842e11ed59a)
- Servo (like [this](https://www.aliexpress.com/item/Micro-9g-servo-RC-SG90-Aircraft-airplane-model-parts-for-Unique-model-Biplane-Helicopter-Accessories/32677485253.html?spm=2114.01010208.3.21.hMGnOQ&ws_ab_test=searchweb0_0,searchweb201602_5_10065_10068_10084_10083_10080_10082_10081_10060_10061_10062_10056_10055_10054_10059_10078_10079_10073_10096_10070_10100_10052_423_10050_10051_424,searchweb201603_8&btsid=b4745c77-5a61-4155-9d28-949cdfefc80d)
- 2x LED (optional)
- 2x 220 Ohm Resistors (only reuired if using LED's)
- 100uF capacitor (optional)
- A few wires
- Black Posterboard (Very light weight)

Instal Python 2.7.12 (download [here](https://www.python.org/downloads/)

Add Python path to PATH (instructions [here](http://stackoverflow.com/questions/3701646/how-to-add-to-the-pythonpath-in-windows-7))

Start a CMD prompt as administrator (instructions [here](https://technet.microsoft.com/en-us/library/cc947813(v=ws.10).aspx)) 

From the CMD prompt we manually install Pip using the following command

`python get-pip.py`

Next we want to install pyserial, again at the CMD prompt we type

`python -m pip install pyserial`

Start the Arduino IDE (download [here](https://www.arduino.cc/en/Main/Software))

Wire up the arduino as follows: 

![alt text][basic]

[basic]: http://i.imgur.com/s5vJ4pn.png

When a serial connection is opened to an Arduino it resets itself, this is a problem for us as the code won’t work as intended, so to get around this we’ll use a 100uF capacitor between the Reset and Ground. This is a simple non-permanent solution, but it does mean that to upload code to the Arduino we need to either press the reset button on the Nano when we’re uploading or temporarily remove the capacitor when uploading.

Connect the Nano to the computer and make a note of the COM port it’s using (in my case i'm using COM6 so we’ll use that in the python code later), this can be found in the Arduino IDE (Tools->Port). Upload the Dust_Cover.ide code to the Arduino. If the Arduino is always connected to the same USB port then the port should not change.

Save the open.py and close.py files on to the host computer that has Python installed, connect the arduino to the host via USB, and then double click the open.py or close.py files. Each will send a command over the serial connection and will light the corresponding LED (White for OPEN, Red for CLOSE). Once this is working we can move on to adding the servo and altering the Arduino code to actually move the dustcover.

**Adding the servo**

Instructions are [here](http://playground.arduino.cc/Learning/SingleServoExample), but all we're doing is:

1. Connect the red from the servo to +5V on Arduino.

2. Connect black/brown from the servo to Gnd on Arduino.

3. Connect white/orange from the servo to Analog 0 on Arduino.

![alt text][servo]

[servo]: http://i.imgur.com/UXRSnkK.png

Now we modify the Arduino code to include the servo. The arduino file is called Dust_Cover_Servo.ide, upload it to the Arduino and change the values for `static int open_angle` and `static int open_angle` to suit what works your configuration. I found my values through trial and error.

Affix the servo to the OTA. If this is all you wanted to acheive then stop here and just run the open and close python scripts to control the dust cover. If you also want to control an LED lightbox then continue below.

**Controlling an LED Lightbox**

To control my flat box (from [AliExpress](https://www.aliexpress.com/item/LED-panel-light-square-lampada-300x300-18W-high-bright-led-indoor-ceiling-lamp-SMD5630-white-warm/1785529655.html)) I bought a 4 relay switch (from [AliExpress](https://www.aliexpress.com/item/Brand-New-5V-4-Channel-Relay-Module-for-Arduino-PIC-ARM-DSP-AVR-Raspberry-Pi/1952619257.html)) and wired it up to be in a Normally Open (NO) format so that when theres no signal from the Arduino the relay is not activating the flat panel.

The Arduino code for this step is called Elentirmo_v0.1.ide, upload it to the Arduino and wire digital Pin 10 on the Arduino to IN1 on Relay Module as below. In my image below i've used an LED in place of a lightbulb as Fritzing didn't have one.

![alt text][relay]

[relay]: http://i.imgur.com/iq4v8A0.png

I've also created a very basic Python GUI to control the Dust Cover and Lightbox, it's called Elentirmo_GUI_v0.1.py. Make sure you've installed Pyserial before running it. You don't forget to make sure you changed the COM port to whichever COM your Arduino is using.

![alt text][GUI1]

[GUI1]: http://i.imgur.com/ZBYA1Sw.png

![alt text][GUI2]

[GUI2]: http://i.imgur.com/v5vNbDZ.png

I'm also working on a method to control the LED lightbox via Sequence Generator Pro using a modified version of Jared's [ArduinoLightbox](https://github.com/jwellman80/ArduinoLightbox) code, once it's ready i'll add it to this guide.

**Future Expansion:**
- How to make sure device is always COM6
- Add capability to switch on/off the DSLR
- Add capability to monitor temperature/humidity and also rainfall
- Add capability to open/close the roof
- Improve the GUI to include jog buttons for open/close and show temp/humidity
- Make PC tweet relay actions
