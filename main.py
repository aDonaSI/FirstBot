from wheel import move_straight, lock_wheel,move
import time
delay=1
for k in range(10):
    move(2,0,delay)
    time.sleep(delay)
lock_wheel()