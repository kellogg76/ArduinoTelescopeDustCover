#!/usr/bin/python

from Tkinter import *

root = Tk()
root.title("Elentirmo Observatory Controller v0.1")
dust_cover_text = StringVar()
dust_cover_text.set('Cover Closed')

flat_box_text = StringVar()
flat_box_text.set('Flat Box Off')

def dust_cover_open():
    print "Opening"
    ## Open a serial connection with Arduino.

    import time

    import serial

    ser = serial.Serial("COM9", 9600)   # Open serial port that Arduino is using

    time.sleep(3)                       # Wait 3 seconds for Arduino to reset

    print ser                           # Print serial config



    print "Sending serial command to OPEN the dust cover."
    ser.write("O")

    print "Opening serial connection."

    ser.close()
    # Reminder to close the connection when finished

    if(ser.isOpen()):

     print "Serial connection is still open."

    dust_cover_label.config(bg="Green")
    dust_cover_text.set('Cover is Open')

def dust_cover_close():
    print "Closing"
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

    dust_cover_label.config(bg="red")
    dust_cover_text.set('Cover is closed')

def flat_on():
    print "Activating flat box"
    ## Open a serial connection with Arduino.

    import time

    import serial

    ser = serial.Serial("COM9", 9600)   # Open serial port that Arduino is using

    time.sleep(3)                       # Wait 3 seconds for Arduino to reset

    print ser                           # Print serial config



    print "Sending serial command to turn on the flat box via relay."
    ser.write("Q")

    print "Opening serial connection."

    ser.close()

    # Reminder to close the connection when finished

    if(ser.isOpen()):

     print "Serial connection is still open."

    flat_box_label.config(bg="Green")
    flat_box_text.set('Flat Box on')

def flat_off():
    print "Dectivating flat box"
    ## Open a serial connection with Arduino.

    import time

    import serial

    ser = serial.Serial("COM9", 9600)   # Open serial port that Arduino is using

    time.sleep(3)                       # Wait 3 seconds for Arduino to reset

    print ser                           # Print serial config



    print "Sending serial command to turn off the flat box via relay."
    ser.write("F")

    print "Opening serial connection."

    ser.close()

    # Reminder to close the connection when finished

    if(ser.isOpen()):

     print "Serial connection is still open."
    flat_box_label.config(bg="red")
    flat_box_text.set('Flat Box Off')

open_dust_cover_btn = Button(text=" Open Cover ", width=15, command=dust_cover_open)
open_dust_cover_btn.grid(row=0, column=0)

close_dust_cover_btn = Button(text=" Close Cover ", width=15, command=dust_cover_close)
close_dust_cover_btn.grid(row=1, column=0)

flat_box_on_btn = Button(text="Turn On Light", width=15, command=flat_on)
flat_box_on_btn.grid(row=0, column=2)

flat_box_off_btn = Button(text="Turn Off Light", width=15, command=flat_off)
flat_box_off_btn.grid(row=1, column=2)

status_label = Label(root, text=("Current Status"), width=15, fg="Black")
status_label.grid(row=2, column=1)

dust_cover_label = Label(root, textvariable=dust_cover_text, width=15, fg="Black", bg="Red")
dust_cover_label.grid(row=2, column=0)

flat_box_label = Label(root, textvariable=flat_box_text, width=15, fg="Black", bg="Red")
flat_box_label.grid(row=2, column=2)

root.mainloop()
