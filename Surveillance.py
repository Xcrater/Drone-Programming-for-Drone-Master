from djitellopy import tello
import KeyPressModule as kp
import time
import cv2

kp.init()
tello = tello.Tello()
tello.connect()
print(tello.get_battery())
global img
tello.streamon()
global direction
direction = 1

#tello.send_command_with_return('downvision 1')

def setVideoDirections():
    direction = 1 - direction
    return direction 
    # tello.send_command_with_return(cmd)

def getKeyboardInput():
    lr, fb, ud, yv = 0, 0, 0, 0
    speed = 50
    
    if kp.getKey("LEFT"): lr = -speed
    elif kp.getKey("RIGHT"): lr = speed

    if kp.getKey("UP"): fb = speed
    elif kp.getKey("DOWN"): fb = -speed

    if kp.getKey("w"): ud = speed
    elif kp.getKey("s"): ud = -speed

    if kp.getKey("a"): yv = -speed
    elif kp.getKey("d"): yv = speed

    if kp.getKey("SPACE"): tello.land()
    if kp.getKey("t"): tello.takeoff()
    
    # Flip in all four direction
    if kp.getKey("i"): tello.flip_forward()
    if kp.getKey("k"): tello.flip_back()
    if kp.getKey("j"): tello.flip_left()
    if kp.getKey("l"): tello.flip_right()

    if kp.getKey("z"):
        cv2.imwrite(f'Resources/TelloImages/{time.time()}.jpg',img)
        time.sleep(0.3)

    #Velocity vector (Vx, Vy, Vz, Wz )
    return [lr, fb, ud, yv]
    
while True:
    velocityVector = getKeyboardInput()
    tello.send_rc_control(velocityVector[0], velocityVector[1], velocityVector[2], velocityVector[3])
    # Frame grabber
    img = tello.get_frame_read().frame
    #Default (720x480)
    img = cv2.resize(img, (360, 240))
    cv2.imshow("Image", img)
    cv2.waitKey(1)
    time.sleep(0.05)
    