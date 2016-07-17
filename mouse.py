#!/usr/bin/python

import struct
import binhex
import gp2y0e02b
x = 0
y = 0

# You'll need to find the name of your particular mouse to put in here.
# Here is how:
# cd /dev/input/by-id/
# Find your mouse and substitute below
file = open("/dev/input/by-id/usb-04f3_PS_2+USB_Mouse-event-mouse","rb")


while True:

    #DistanceSensor = gp2y0e02b.GP2Y0E02B()
    #print DistanceSensor.value()
    byte = file.read(16)
    #h = ":".join("{:02x}".format(ord(c)) for c in byte)
    #print "byte=",h

    (type,code,value) =  struct.unpack_from('hhi', byte, offset=8)
    #print 'type = %d, code = %d, value = %d' % (type, code, value)

    if type == 1 and value == 1:
        servo = open("/dev/pi-blaster", "w")
        if code == 272:
            print "LEFT PRESS"
            servo.write('17=0.01\n')
            servo.write('22=0.01\n')
        if code == 273:
            print "RIGHT PRESS"
            servo.write('17=0.19\n')
            servo.write('22=0.19\n')
        servo.close()

    if type == 2:
        if code == 8:
            print "SCROLL",value
        if code == 0:
            print "MOVE L/R",value    
            '''
            # limit the value of x to 1 - 20 (0.1 - 0.2)
            if(x < 0.2 and value > 0):
                x = x + 0.001
            if(x > 0 and value < 0):
                x = x - 0.001                
            if x > 0.2:
               x = 0.2
            if x < 0.001:
               x = 0.001
            print 'x=%.2f' %x
            servo = open("/dev/pi-blaster", "w")
            servo.write('17=%s\n' %str(x))
            servo.close()
            '''
        if code == 1:
            print "MOVE U/D",value
            '''
            # limit the value of x to 1 - 20 (0.1 - 0.2)
            if(y < 0.2 and value > 0):
                y = y + 0.001
            if(y > 0 and value < 0):
                y = y - 0.001                
            if y > 0.2:
               y = 0.2
            if y < 0.001:
               y = 0.001
            print 'y=%.2f' %y
            servo = open("/dev/pi-blaster", "w")
            servo.write('22=%s\n' %str(y))
            servo.close()   
'''            