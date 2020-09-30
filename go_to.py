from wheel import move, lock_wheel
import time
x0=0
y0=0
angle0=0
delay=1
speed=2
ang_speed=3.14/10
lin_speed=20

def go_to(x,y,angle):
    move(x-x0,0,(x-x0)/lin_speed)
    time.sleep((x-x0)/lin_speed)
    move(0,90,90/ang_speed)
    time.sleep(90/ang_speed)
    move(y-y0,0,(y-y0)/lin_speed)
    time.sleep((y-y0)/lin_speed)
    move(0,-90,-90/ang_speed)
    time.sleep(-90/ang_speed)
    move(0,angle-angle0,(angle-angle0)/ang_speed)
    time.sleep((angle-angle0)/ang_speed)
    lock_wheel()

    x0=x0-x
    y0=y0-y
    angle0=angle0-angle


