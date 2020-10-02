import pypot.dynamixel
import time
import sched
import math
import matplotlib.pyplot as plt
from wheel import get_speed

LjauneX=[]
LjauneY=[]
LbleuX=[]
LbleuY=[]
LrougeX=[]
LrougeY=[]




#dt = 0.1
r = 2.6
currenttime=0

def direct_kinematics(vg,vd) :
    vd=-vd * r * 2 * math.pi / 44.81  #même sens positif que la roue gauche
    vg *= r * 2 * math.pi / 44.81
    vmin, vmax = min(vg, vd), max(vg, vd)
    xpoint=vmin + (vmax-vmin)/2
    thetapoint=(vd-vg)/18
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

def odom_update():
    global x, y, theta

    if currenttime == 0 :
        dt = 0.1
        currenttime = time.time()
    else :
        prectime = currenttime
        currenttime = time.time()
        dt = currenttime - prectime

    x,y,theta = calc_odom(dt, x,y,theta)

def odom_follow(couleur) :
    odom_update()
    if couleur == 0 :
        LjauneX.append(x)
        LjauneY.append(y)
    elif couleur == 1 :
        LbleuX.append(x)
        LbleuY.append(y)
    elif couleur == 1 :
        LrougeX.append(x)
        LrougeY.append(y)

def print_circuit() :
    plt.plot(LjauneX,LjauneY,color='y')
    plt.plot(LbleuX,LbleuY,color='b')
    plt.plot(LrougeX, LrougeY, color='r')
    plt.show()


def odom_get():
    return x, y, theta
