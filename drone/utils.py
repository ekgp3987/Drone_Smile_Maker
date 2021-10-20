from djitellopy import Tello
import cv2
import time

def initTello():
    myDrone = Tello() 
    myDrone.connect() # dron connection

    # set all speed to 0
    myDrone.for_back_velocity = 0
    myDrone.left_right_velocity = 0
    myDrone.up_down_velocity = 0
    myDrone.yaw_velocity = 0
    myDrone.speed = 0

    print("\n * Drone battery percentage : " + str(myDrone.get_battery()) + "%")

    return myDrone