from wheel import move, lock_wheel
from odom import calc_odom
import time
import math
x0=0
y0=0
angle0=0
delay=1
speed=2
ang_speed=3.14/2
lin_speed=15
image_width=320.0


def go_to(x,y,angle):
    global x0,y0,angle0,delay,speed,ang_speed,lin_speed


    move(x-x0,0,abs(x-x0)/lin_speed)
    time.sleep(abs(x-x0)/lin_speed)

    move(0,math.pi/2,abs(3.14/2)/ang_speed)
    time.sleep(abs(3.14/2)/ang_speed)

    move(y-y0,0,abs(y-y0)/lin_speed)
    time.sleep(abs(y-y0)/lin_speed)

    move(0,-math.pi/2,abs(-3.14/2)/ang_speed)
    time.sleep(abs(-3.14/2)/ang_speed)

    move(0,angle-angle0,abs(angle-angle0)/ang_speed)
    time.sleep(abs(angle-angle0)/ang_speed)

    lock_wheel()

    x0=x0-x
    y0=y0-y
    angle0=angle0-angle

def angle_correction(angle):
    while angle>math.pi:
        angle-=math.pi*2
        
    while angle<-math.pi:
        angle+=math.pi*2
        
    return angle

def go_to_fancy(x,y,angle):
    global x0,y0,angle0,delay,speed,ang_speed,lin_speed
    corr_angle=angle0+math.atan2((y+y0),(x+x0))
    corr_angle=angle_correction(corr_angle)
    move(0,corr_angle ,abs(corr_angle)/ang_speed)
    time.sleep(abs(corr_angle)/ang_speed)

    distance=math.sqrt((y+y0)**2+(x+x0)**2)
    move(distance,0,abs(distance)/lin_speed)
    time.sleep(abs(distance)/lin_speed)
    dest_angle=angle-angle0-corr_angle
    dest_angle=angle_correction(dest_angle)
    move(0,dest_angle,abs(dest_angle)/ang_speed)
    time.sleep(abs(dest_angle)/ang_speed)
    lock_wheel()
    x0=-x
    y0=-y
    angle0=-angle

def follow(distance,delay):
    ratio=distance/image_width
    ratio=(0.5-ratio)*2
    move(lin_speed*delay*(1-abs(ratio)), ang_speed*delay*ratio,delay)

