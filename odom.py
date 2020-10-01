import pypot.dynamixel
import time
import sched
import math


#dt = 0.1
r = 2.6

def direct_kinematics(vg,vd) :
    vd=-vd * r * 2 * math.pi / 44.81  #même sens positif que la roue gauche
    vg *= r * 2 * math.pi / 44.81
    xpoint=vd + (vd-vg)/2
    thetapoint=(vd-vg)/r
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
    vd, vg = dxl_io.get_present_speed([1,2])
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
