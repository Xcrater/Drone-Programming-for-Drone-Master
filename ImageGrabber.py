from djitellopy import Tello
import cv2

# Connect to Tello
tello = Tello()
tello.connect()

# Battery Status
print(tello.get_battery())

# This stream will give us all frames one by one
tello.streamon()

# To grab frames continuously
while True:

    # Down facing camera - Grayscale 320x240 IR sensive camera
    tello.send_command_without_return('downvision 1')
    img = tello.get_frame_read().frame
    #Default (720x480)
    #img = cv2.resize(img, (360, 240))
    cv2.imshow("Image", img)
    cv2.waitKey(1)
    