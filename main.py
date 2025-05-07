#!/usr/bin/env pybricks-micropython
# Before running this program, make sure the client and server EV3 bricks
# are paired using Bluetooth, but do NOT connect them. The program will
# take care of establishing the connection.
# The server must be started before the client!
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor
from pybricks.parameters import Port, Stop, Direction
from pybricks.tools import wait, StopWatch
from pybricks.messaging import BluetoothMailboxClient, TextMailbox
from pybricks.robotics import DriveBase

ev3 = EV3Brick()
left_motor = Motor(Port.D)
right_motor = Motor(Port.A)
lift_motor = Motor(Port.B)
claw_motor = Motor(Port.C)
claw_motor.control.stall_tolerances(100,10)


# This is the name of the remote EV3 or PC you are connecting to.
SERVER = 'ev3dev'
client = BluetoothMailboxClient()
mbox = TextMailbox('greeting', client)
print('establishing connection...')
client.connect(SERVER)
print('connected!')

# In this program, the client sends the first message and then waits for the
# server to reply.
mbox.send('hello!')
mbox.wait()
print(mbox.read())

robot = DriveBase(left_motor, right_motor, wheel_diameter=55.5, axle_track=104)

claw_open = True


while True:

    if mbox.read() == 'forward':
        robot.straight(2)
    elif mbox.read()=='fast_forward':
        robot.drive(200, 0)
    elif mbox.read() == 'backward':
        robot.straight(-2)
    elif mbox.read() == 'fast_backward':
        robot.drive(-200, 0)
    elif mbox.read()=="left_fast":
        robot.drive(0, -25)
    elif mbox.read() == 'left':
        robot.drive(0, -2)
    elif mbox.read() == 'right_fast':
        robot.drive(0, 25)
    elif mbox.read() == 'right':
        robot.drive(0, 2)
    elif mbox.read() == 'stop':
        robot.stop()
    elif mbox.read() == 'claw_open':
        claw_motor.run(100)
    elif mbox.read() == 'claw_close':   
        claw_motor.run(-100)
    elif mbox.read()=='lift':
        lift_motor.run(20)
    elif mbox.read()=='drop':    
        lift_motor.run(-20)
    elif mbox.read() == 'claw_stop':
        claw_motor.stop(Stop.HOLD)
    elif mbox.read() == 'lift_stop':
        lift_motor.stop(Stop.HOLD)
    else:
        robot.stop()
    wait(10)