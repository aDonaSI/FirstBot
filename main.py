from wheel import move_straight, lock_wheel,move
import time
delay=0.1
for k in range(100):
    move(2,3.14/100,delay)
    time.sleep(delay)
lock_wheel()

# move(20,0,5)

# #move_straight(44.81)
# time.sleep(5)
# lock_wheel()