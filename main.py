from wheel import move_straight, lock_wheel,move,free_wheel
from go_to import go_to,go_to_fancy,follow
from suivi import get_distance_suivi, get_current_color, end_camera
from odom import odom_update, odom_get, idk

import time
import math


delay=0.1
# for k in range(10):
#     move(20,3.14/10,delay)
#     time.sleep(delay)
# lock_wheel()

# go_to(8,-5,(3.14/4))
# lock_wheel()
# go_to(-8,5,-(3.14/4))
# lock_wheel()

# try:
#     x, y, angle = go_to_fancy(10, 10, 0)
#     print(x, y, angle)
#     free_wheel()
# except Exception as e:
#     lock_wheel()
#     print(e)

def odom():
    while True:
        odom_update(.1)
        print(odom_get())
        time.sleep(.1)


def follow_line():
    while 1:
        t0 = time.time()
        distance = get_distance_suivi()
        #odom_qqch(get_current_color())
        t1 = time.time()
        follow(distance, t1-t0)

follow_line()
end_camera()

#idk()

# time.sleep(2)
# go_to_fancy(10,-10,(3.14))
# lock_wheel()
# time.sleep(2)
# go_to_fancy(0,0,0)
# free_wheel()

# move(20,0,5)

# #move_straight(44.81)
# time.sleep(5)
# lock_wheel()

# for k in range(10):
#     follow(160,delay)
#     time.sleep(delay)

# for k in range(10):
#     follow(160-(k*16),delay)
#     time.sleep(delay)
# free_wheel()


