import pypot.dynamixel
import time
import sched
import math
from wheel import get_speed


#dt = 0.1
r = 2.6

def direct_kinematics(vg,vd) :
    vd=-vd * r * 2 * math.pi / 44.81  #même sens positif que la roue gauche
    vg *= r * 2 * math.pi / 44.81
    vmin, vmax = min(vg, vd), max(vg, vd)
    xpoint=vmin + (vmax-vmin)/2
    thetapoint=(vd-vg)/17.9
    return xpoint,thetapoint

def odom(dt, xpoint,thetapoint) :
    dx = xpoint * dt * math.cos(thetapoint * dt)
    dy = xpoint * dt * math.sin(thetapoint * dt)
    dtheta = thetapoint * dt
    return dx,dy,dtheta

def odom_tick(xprec, yprec, thetaprec, dx, dy ,dtheta) :
    theta = thetaprec + dtheta
    x = xprec + dx * math.cos(theta) + dy * math.sin(theta)
    y = yprec + dx * math.sin(theta) - dy * math.cos(theta)
    return x,y,theta

def calc_odom (dt, xprec,yprec,thetaprec) :
    vd, vg = get_speed()
    xpoint, thetapoint = direct_kinematics(vg,vd)
    dx,dy,dtheta = odom(dt, xpoint, thetapoint)
    return odom_tick(xprec,yprec,thetaprec,dx,dy,dtheta)


start = time.time()

Nstep = 0

x = 0
y = 0
theta = 0

def odom_update(dt):
    global x, y, theta
    x,y,theta = calc_odom(dt, x,y,theta)

def odom_get():
    return x, y, theta

def idk():
    dt = .1
    Nstep = 0

    x = 0
    y = 0
    theta = 0
    while (1) :
        ctime = time.time() - start
        if (Nstep*0.1 - round(ctime,3) < 0.01) :
            x,y,theta = calc_odom(dt, x,y,theta)
            print (round(x,3),round(y,3),round(theta,3))
            Nstep += 1