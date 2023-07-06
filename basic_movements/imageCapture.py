from djitellopy import tello
import cv2

me = tello.Tello()
me.connect()

print(me.get_battery())
me.streamon()

while True:
    img = me.get_frame_read().frame
    img = cv2.resize(img, (360, 240))
    im_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    cv2.imshow("Image", im_rgb)
    cv2.waitKey(1)
