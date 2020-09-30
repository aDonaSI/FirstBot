import pypot.dynamixel
speed=0
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
