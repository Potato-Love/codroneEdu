from codrone_edu.drone import *
from time import sleep
Drone = Drone()
Drone.pair()


Drone.takeoff()
Drone.move_distance(0, 0, 0.8, 0.5)
Drone.move_forward(0.5, 'm', 0.5)
Drone.move_left(0.5, 'm', 0.5)
Drone.move_backward(0.5, 'm', 0.5)
Drone.move_right(0.5, 'm', 0.5)
Drone.move_forward(1, 'm', 0.5)


Drone.land()
Drone.close()