from codrone_edu.drone import *
from time import sleep
Drone = Drone()
Drone.pair()


def buzzer(n):
    if n == 0:
        for i in range(5):
            Drone.start_drone_buzzer(500)
            time.sleep(0.3)
            Drone.stop_drone_buzzer()
    else:
        for i in range(5):
            Drone.drone_buzzer(400, 300)
            time.sleep(0.3)

def A():
    Drone.move_distance(1.2, 0, 0.3, 0.7)
    Drone.move_distance(1, 0, -0.6, 0.7)
    Drone.move_distance(0, 0 ,  1, 0.5)
    Drone.move_distance(1.1, 0, 0, 0.7)
    Drone.move_distance(1, 0, -1.2, 0.7)
    Drone.move_distance(0.2, 0, 1.5, 0.5)
    Drone.turn_degree(90, 2, 20)

def B():
    Drone.move_distance(1, 0, 0, 0.5)
    Drone.move_forward(0.5, 'm', 0.5)
    Drone.move_left(0.5, 'm', 0.5)
    Drone.move_backward(0.5, 'm', 0.5)
    Drone.move_right(0.5, 'm', 0.5)
    Drone.move_forward(1.2, "m", 0.5)    
    Drone.turn_left()
def C():
    Drone.move_forward(distance=3.2, units="m", speed=1)

def sorting():
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

Drone.reset_gyro()
Drone.reset_sensor()
Drone.set_trim(0, 0)  # 트림 초기화
sleep(2)
buzzer(0)
Drone.takeoff()

A()
#buzzer(1)
B()
#buzzer(0)
sorting()
C()

Drone.land()
Drone.close()