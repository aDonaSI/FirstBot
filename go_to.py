from wheel import move, lock_wheel
import time
x0=0
y0=0
angle0=0
delay=1
speed=2
ang_speed=3.14/5
lin_speed=20

def go_to(x,y,angle):
    global x0,y0,angle0,delay,speed,ang_speed,lin_speed
    move(x-x0,0,abs(x-x0)/lin_speed)
    time.sleep(abs(x-x0)/lin_speed)

    move(0,3.14/2,abs(3.14/2)/ang_speed)
    time.sleep(abs(3.14/2)/ang_speed)

    move(y-y0,0,abs(y-y0)/lin_speed)
    time.sleep(abs(y-y0)/lin_speed)

    move(0,-3.14/2,abs(-3.14/2)/ang_speed)
    time.sleep(abs(-3.14/2)/ang_speed)

    move(0,angle-angle0,abs(angle-angle0)/ang_speed)
    time.sleep(abs(angle-angle0)/ang_speed)

    lock_wheel()

    x0=x0-x
    y0=y0-y
    angle0=angle0-angle


