from wheel import move_straight, lock_wheel,move,free_wheel
from go_to import go_to,go_to_fancy
import time

# delay=1
# for k in range(10):
#     move(20,3.14/10,delay)
#     time.sleep(delay)
# lock_wheel()

# go_to(8,-5,(3.14/4))
# lock_wheel()
# go_to(-8,5,-(3.14/4))
# lock_wheel()

go_to_fancy(10,10,(3.14))
lock_wheel()
time.sleep(2)
go_to_fancy(10,-10,(3.14))
lock_wheel()
time.sleep(2)
go_to_fancy(0,0,0)
free_wheel()

# move(20,0,5)

# #move_straight(44.81)
# time.sleep(5)
# lock_wheel()