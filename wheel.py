import pypot.dynamixel
speed=0
robot_width=18
ports = pypot.dynamixel.get_available_ports()
if not ports:
    exit('No port')

dxl_io = pypot.dynamixel.DxlIO(ports[0])
dxl_io.set_wheel_mode([1,2])

def free_wheel():
    dxl_io.set_joint_mode([1,2])

def lock_wheel():
    dxl_io.set_wheel_mode([1,2])
    dxl_io.set_moving_speed({1: 0,2:0})

def move_straight(speed):
    dxl_io.set_moving_speed({1: -speed,2:speed})

def move(distance, angle, delay):
    if angle <0 :
        dis_left=distance-((abs(angle)*robot_width))
        dis_right=distance+((abs(angle)*robot_width))
    elif angle>0 :
        dis_left=distance+((abs(angle)*robot_width))
        dis_right=distance-((abs(angle)*robot_width))
    else :
        dis_left=dis_right=distance

    speed_left=(dis_left/delay)/2.6
    speed_right= (dis_right/delay)/2.6

    dxl_io.set_moving_speed({1: -(speed_right/1.339),2:(speed_left/1.339)})