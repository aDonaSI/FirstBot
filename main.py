from wheel import move_straight, lock_wheel,move,free_wheel
from go_to import go_to,go_to_fancy,follow
from suivi import get_distance_suivi, get_current_color, end_camera
from odom import odom_update, odom_get, print_circuit

import time
import math
import sys


def time_exec(f, args):
    before = time.time()
    f(args)
    return time.time() - before



def task_follow():
    while 1:

        t0 = time.time()
        distance, color = get_distance_suivi()
        t1 = time.time()

        lock_wheel()
        print("ratio:", (0.5-distance/160)*2, "is color:", color, "time:", t1-t0)
        #if input("Press Enter to continue..."): break

        follow(distance, t1-t0)
        #time.sleep(2)

def task_goto(x, y, theta):
    go_to_fancy(x, y, theta)

def task_odom():
    free_wheel()
    dt = .1
    def loop():
        odom_update(dt)
        print(odom_get())

    while True:
        time_cost = time_exec(loop)
        time.sleep(dt - time_cost)



## __main__
if len(sys.argv) > 1:
    if sys.argv[1] == "follow":
        task_follow()

    elif sys.argv[1] == "goto":
        x, y, theta = float(sys.argv[2]), float(sys.argv[3]), float(sys.argv[4])
        task_goto()

    elif sys.argv[1] == "odom":
        task_odom()

end_camera()
