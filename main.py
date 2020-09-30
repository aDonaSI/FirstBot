from wheel import move_straight, lock_wheel,move
import time
delay=1
for k in range(10):
    move(0,1/10,delay)
    time.sleep(delay)