from codrone_edu.drone import *
from time import sleep
Drone = Drone()
Drone.pair()


def buzzer():
    for i in range(5):
        Drone.start_drone_buzzer(500)
        time.sleep(0.3)
        Drone.stop_drone_buzzer()

def A():
    Drone.move_distance(1.2, 0, 0.3, 0.5)
    Drone.move_distance(0.9, 0, -0.6, 0.5)
    Drone.move_distance(0, 0 ,  1, 0.5)
    Drone.move_distance(0.8, 0, 0, 0.5)
    Drone.move_distance(0.8, 0, -1, 0.5)
    Drone.move_distance(0.1, 0, 0.8, 0.5)
    Drone.turn_degree(90, 2, 20)

def B():
    Drone.move_distance(1, 0, 0, 1)
    Drone.square(30, 1, -1)
    Drone.move_forward(distance=1.5, units="m", speed=0.5)    

def C():
    Drone.move_forward(distance=3.2, units="m", speed=1)

def sorting():
    Drone.turn_degree(90, 2, 20)
    Drone.hover(20)

    with open("unsorted integer.txt", "r", encoding="utf-8") as file:
        lines = file.readlines()

    def quick_sort(arr):
        if len(arr) <= 1:
            return arr
        pivot = arr[0]
        left = [x for x in arr[1:] if x > pivot]      
        right = [x for x in arr[1:] if x <= pivot]    
        return quick_sort(left) + [pivot] + quick_sort(right)

    sorted = quick_sort(lines)
    with open("SB-a04-1-sorted_out.txt", "w", encoding="utf-8") as f:
        for num in sorted:
            f.write(f"{num}")

#buzzer()
Drone.reset_gyro()
Drone.reset_sensor()
Drone.takeoff()

A()
#buzzer()
Drone.hover(2)
B()
#buzzer
sorting()
C()

Drone.land()
Drone.close()