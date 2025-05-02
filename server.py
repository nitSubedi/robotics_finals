#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor
from pybricks.parameters import Port, Stop, Direction
from pybricks.tools import wait
from pybricks.messaging import BluetoothMailboxServer, TextMailbox

ev3 = EV3Brick()
left_motor = Motor(Port.D)
right_motor = Motor(Port.A)
claw_motor = Motor(Port.B)

server = BluetoothMailboxServer()
mbox = TextMailbox('command', server)

ev3.screen.print('Waiting for connection...')
server.wait_for_connection()
ev3.screen.print('Connected!')

# movement functions
def forward(speed=500):
    left_motor.run(speed)
    right_motor.run(speed)

def backward(speed=500):
    left_motor.run(-speed)
    right_motor.run(-speed)

def left(speed=500):
    left_motor.run(-speed)
    right_motor.run(speed)

def right(speed=500):
    left_motor.run(speed)
    right_motor.run(-speed)

# claw functions
def open_claw():
    claw_motor.run_angle(200, 90, then=Stop.HOLD, wait=True) 

def close_claw():
    claw_motor.run_angle(200, -90, then=Stop.HOLD, wait=True)  

# main loop
while True:
    mbox.wait()
    cmd = mbox.read()
    ev3.screen.clear()
    ev3.screen.print('Cmd:', cmd)

    if cmd == 'forward':
        forward()
    elif cmd == 'backward':
        backward()
    elif cmd == 'left':
        left()
    elif cmd== 'right':
        right()
    elif cmd == 'pickup':
        close_claw()
    elif cmd == 'release':
        open_claw()

