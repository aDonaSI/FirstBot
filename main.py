from wheel import move_straight, lock_wheel,move,free_wheel
from go_to import go_to,go_to_fancy,follow
import suivi
import time
import math

from odom import odom_update, odom_get, idk

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
    while True:
        ret, frame = cap.read()
        src = frame[160:]
        green_processing(frame)
        dataset = color_pixel_coord(frame)

        if (len(dataset)>0):
            centers = kmeans(dataset,2)
            lastcenter = behavior(centers,lastcenter)
            follow(lastcenter,delay)
    #Testing
            cv2.circle(src,(int(centers[0][1]),int(centers[0][0])),1,(255,0,255),3)
            cv2.circle(src,(int(centers[1][1]),int(centers[1][0])),1,(255,0,255),3)
        print("COLOR = ",COLOR,"\n")
        cv2.imshow("Frame", src)
    #EO Testing

        key = cv2.waitKey(1)
        if key==50:
            free_wheel()
            break


follow_line()

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


