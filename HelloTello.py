# -*- coding: utf-8 -*-
# @Author: accioo
# @Date:   2022-06-02 15:53:38
# @Last Modified by:   accioo
# @Last Modified time: 2022-06-02 16:02:18
from djitellopy import Tello
from time import sleep

tello = Tello()
tello.connect()

print(tello.get_battery())

tello.takeoff()

# Go forward for 30 cm
#tello.move_forward(30)

# Go forward at 40cm/sec seed for 2 seconds
tello.send_rc_control(0, 40, 0, 0)
sleep(3)

# Go right at 30cm/sec speed for 3 seconds
tello.send_rc_control(30, 0, 0, 0)
sleep(3)

# Rotate clockwise at 40deg/sec speed for 2 seconds
tello.send_rc_control(0, 0, 0, 40)
sleep(2)

# Stop first and then land 
tello.send_rc_control(0, 0, 0, 0)
sleep(2)

tello.land()