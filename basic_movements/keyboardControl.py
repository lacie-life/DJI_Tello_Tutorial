from djitellopy import tello
import KeyPressModule as kp
from time import sleep

kp.init()
me = tello.Tello()
me.connect()

print(me.get_battery())

def getKeyboardInput():
    lr, fb, ud, yv = 0, 0, 0, 0
    speed = 50
    if kp.getKey("LEFT"): # left
        lr = -speed
    elif kp.getKey("RIGHT"): # right
        lr = speed
    if kp.getKey("UP"): # forward
        fb = speed
    elif kp.getKey("DOWN"): # backward
        fb = -speed
    if kp.getKey("w"): # up
        ud = speed
    elif kp.getKey("s"): # down
        ud = -speed
    if kp.getKey("a"): # left yaw
        yv = -speed
    elif kp.getKey("d"): # right yaw
        yv = speed
    if kp.getKey("q"):
        me.land()
        sleep(3)
    if kp.getKey("e"):
        me.takeoff()
    return [lr, fb, ud, yv]

while True:
    vals = getKeyboardInput()
    me.send_rc_control(vals[0], vals[1], vals[2], vals[3])
    sleep(0.05)


