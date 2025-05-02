#!/usr/bin/env pybricks-micropython
from pybricks.messaging import BluetoothMailboxClient, TextMailbox
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import TouchSensor, Motor
from pybricks.parameters import Port, Button

# initalizations
ev3 = EV3Brick()
client = BluetoothMailboxClient()
mbox = TextMailbox('command', client)

# connect to server
SERVER = 'ev3dev'
print('Connecting to server...')
client.connect(SERVER)
print('Connected!')

# keep track of the last button pressed
last_button = None
claw_closed = False # start with claw open

# main loop
while True:
    pressed = ev3.buttons.pressed()

    if Button.UP in pressed and last_button != Button.UP:
        mbox.send('forward')
        ev3.screen.clear()
        ev3.screen.print('Sent: forward')
        last_button = Button.UP

    elif Button.DOWN in pressed and last_button != Button.DOWN:
        mbox.send('backward')
        ev3.screen.clear()
        ev3.screen.print('Sent: backward')
        last_button = Button.DOWN

    elif Button.LEFT in pressed and last_button != Button.LEFT:
        mbox.send('left')
        ev3.screen.clear()
        ev3.screen.print('Sent: left')
        last_button = Button.LEFT

    elif Button.RIGHT in pressed and last_button != Button.RIGHT:
        mbox.send('right')
        ev3.screen.clear()
        ev3.screen.print('Sent: right')
        last_button = Button.RIGHT

    elif Button.CENTER in pressed and last_button != Button.CENTER:
        if claw_closed:
            mbox.send('release')
            ev3.screen.clear()
            ev3.screen.print('Sent: release')
            claw_closed = False
        else:
            mbox.send('pickup')
            ev3.screen.clear()
            ev3.screen.print('Sent: pickup')
            claw_closed = True
        last_button = Button.CENTER

    # if no button is pressed, clear the screen and reset the last 
    elif not pressed:
        last_button = None

    wait(100)

