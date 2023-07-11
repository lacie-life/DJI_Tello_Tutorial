from djitellopy import tello
import cv2

# Connect to Tello
me = tello.Tello()
me.connect()
print(me.get_battery())

# Get the stream
me.streamon()

while True:
    # Get the image from the stream
    img = me.get_frame_read().frame

    # Resize the image
    img = cv2.resize(img, (360, 240))
    cv2.imshow("Image", img)
    cv2.waitKey(1)

