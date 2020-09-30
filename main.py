from wheel import move_straight, lock_wheel
import time

move_straight(10)
time.sleep(5)
move_straight(-10)
time.sleep(5)
lock_wheel()