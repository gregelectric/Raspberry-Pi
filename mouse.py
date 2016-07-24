#!/usr/bin/python

import struct
import binhex
import smbus
import time

bus = smbus.SMBus(1)    # 0 = /dev/i2c-0 (port I2C0), 1 = /dev/i2c-1 (port I2C1)
distance = 0  
servo_angle = 0.012  
servo_direction = 1
x = 0
y = 0

# You'll need to find the name of your particular mouse to put in here.
# Here is how:
# cd /dev/input/by-id/
# Find your mouse and substitute below
file = open("/dev/input/by-id/usb-04f3_PS_2+USB_Mouse-event-mouse","rb")

while True:
    # Pan Servo 180 degrees
    if (servo_angle > 0.12 and servo_direction == 1):
        servo_direction = 0
    elif (servo_angle < 0.03 and servo_direction == 0):
        servo_direction = 1
     
    if(servo_direction == 1): 
        servo_angle = servo_angle + 0.005
    else:
        servo_angle = servo_angle - 0.005
   
    #print 'servo angle=%.3f' %servo_angle
    servo = open("/dev/pi-blaster", "w")
    servo.write('22=%s\n' %str(servo_angle))
    servo.close()
    time.sleep(0.1)

    distance = bus.read_i2c_block_data(0x40, 0x5E, 1)
    distance2 = float(distance.pop(0))
    print 'distance=%.2f' %distance2       
"""
    byte = file.read(16)
    #h = ":".join("{:02x}".format(ord(c)) for c in byte)
    #print "byte=",h

    (type,code,value) =  struct.unpack_from('hhi', byte, offset=8)
    #print 'type = %d, code = %d, value = %d' % (type, code, value)

    if type == 1 and value == 1:
        servo = open("/dev/pi-blaster", "w")
        if code == 272:
            print "LEFT PRESS"
            servo.write('17=0.012\n')
        if code == 273:
            print "RIGHT PRESS"
            servo.write('17=0.03\n')
        servo.close()
    if type == 2:
        if code == 8:
            print "SCROLL",value
        if code == 0:
            print "MOVE L/R",value    
        if code == 1:
            print "MOVE U/D",value 
"""            