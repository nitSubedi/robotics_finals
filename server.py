#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction,Button, Color
from pybricks.tools import wait, StopWatch, DataLog

from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
from pybricks.messaging import BluetoothMailboxServer, TextMailbox
server = BluetoothMailboxServer()
mbox = TextMailbox('greeting', server)
# The server must be started before the client!
print('waiting for connection...')
server.wait_for_connection()
print('connected!')
# In this program, the server waits for the client to send the first message
# and then sends a reply.
mbox.wait()
print(mbox.read())
mbox.send('hello to you!')

ev3 = EV3Brick()



# keep track of the last button pressed
last_button = None
claw_closed = False # start with claw open



# main loop
while True:
    
    ev3.screen.clear()
    button = ev3.buttons.pressed()
    ev3.screen.print(button)
    print(button)

    if Button.CENTER in button:
        if Button.UP in button:
            while Button.UP in button:
                button = ev3.buttons.pressed()
                mbox.send('claw_open')
                wait(500)
                ev3.screen.clear()
                ev3.screen.print('Sent: claw_open')
            mbox.send('claw_stop')
        elif Button.DOWN in button:
            while Button.DOWN in button:
                button = ev3.buttons.pressed()
                mbox.send('claw_close')
                wait(500)
                ev3.screen.clear()
                ev3.screen.print('Sent: claw_close')
            mbox.send('claw_stop')
        elif Button.LEFT in button:
            while Button.LEFT in button:
                button = ev3.buttons.pressed()
                mbox.send('lift')
                wait(500)
                ev3.screen.clear()
                ev3.screen.print('Sent: lift')
            mbox.send('lift_stop')
        elif Button.RIGHT in button:
            while Button.RIGHT in button:
                button = ev3.buttons.pressed()
                mbox.send('drop')
                wait(500)
                ev3.screen.clear()
                ev3.screen.print('Sent: drop')
            mbox.send('lift_stop')
        while Button.CENTER in ev3.buttons.pressed():
            wait(50)
        wait(100)

    if Button.UP in button:
        while Button.UP in button:
            button = ev3.buttons.pressed()
            mbox.send('forward')
            wait(500)
            ev3.screen.clear()
            ev3.screen.print('Sent: forward')
        ev3.screen.clear()
        mbox.send('stop')
#
    if Button.DOWN in button:
        while Button.DOWN in button:
            button = ev3.buttons.pressed()
            mbox.send('backward')
            wait(500)
            ev3.screen.clear()
            ev3.screen.print('Sent: backward')
        ev3.screen.clear()
        mbox.send('stop')
  
    if Button.LEFT in button:
        while Button.LEFT in button:
            button = ev3.buttons.pressed()
            mbox.send('left')
            wait(500)
            ev3.screen.clear()
            ev3.screen.print('Sent: left')
        ev3.screen.clear()
        mbox.send('stop')
    if Button.RIGHT in button:
        while Button.RIGHT in button:
            button = ev3.buttons.pressed()
            mbox.send('right')
            wait(500)
            ev3.screen.clear()
            ev3.screen.print('Sent: right')
        ev3.screen.clear()
        mbox.send('stop')
    
#
    
    #elif Button.LEFT_UP in pressed and last_button != Button.CENTER:
    #    mbox.send('pickup')
    #    ev3.screen.clear()
    #    ev3.screen.print('Sent: pickup')
    #    last_button = Button.LEFT_UP
    #    
    ## if no button is pressed, clear the screen and reset the last 
    #elif not pressed:
    #    last_button = None
#
    #wait(100)

