## Open a serial connection with Arduino.
import time
import serial
ser = serial.Serial("COM9", 9600)   # Open serial port that Arduino is using
time.sleep(3)                       # Wait 3 seconds for Arduino to reset
print ser                           # Print serial config


print "Sending serial command to CLOSE the dust cover."
ser.write("C")
print "Closing serial connection."
ser.close()
# Reminder to close the connection when finished
if(ser.isOpen()):
   print "Serial connection is still open."
