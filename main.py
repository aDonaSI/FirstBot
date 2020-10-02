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


def follow_line():
    while 1:
        lock_wheel()
        t0 = time.time()
        distance = get_distance_suivi()
        #odom_qqch(get_current_color())
        t1 = time.time()
        print("time cost:", t1-t0, "distance image:", distance)
        follow(80-distance, .5)
        time.sleep(.5)


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
