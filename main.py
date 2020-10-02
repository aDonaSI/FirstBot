from wheel import move_straight, lock_wheel,move,free_wheel
from go_to import go_to,go_to_fancy,follow
from suivi import get_distance_suivi, get_current_color, end_camera
from odom import odom_update, odom_get, print_circuit

import time
import math


def time_exec(f, args):
    before = time.time()
    f(args)
    return time.time() - before


list_voila = []

def follow_line():
    while 1:
        #lock_wheel()
        t0 = time.time()
        distance, color = get_distance_suivi()
        #odom_qqch(get_current_color())
        t1 = time.time()
        
        ratio=distance/160
        ratio=(0.5-ratio)*2
        print("ratio:", ratio, "is color:", color, "time:", t1-t0)
        #print("time cost:", t1-t0, "distance image:", distance)
        
        list_voila.append(distance)
        if len(list_voila) > 10:
            list_voila.pop(0)
        da, n = 0.0, 1
        for k in range(len(list_voila)):
            da+= list_voila[k]*k
            n+= k
        follow(da/n, t1-t0)
        #time.sleep(.5)


def task_goto(x, y, theta):
    go_to_fancy(x, y, theta)

def task_odom():
    dt = .1
    def loop():
        odom_update(dt)
        print(odom_get())

    while True:
        time_cost = time_exec(loop)
        time.sleep(dt - time_cost)


follow_line() # tmp

## __main__
# if sys.argv[1] == "follow":
#     task_follow()
#
# elif sys.argv[1] == "goto":
#     x, y, theta = float(sys.argv[2]), float(sys.argv[3]), float(sys.argv[4])
#     task_goto()
#
# elif sys.argv[1] == "odom":
#     task_odom()

end_camera()
