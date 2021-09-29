import pyautogui
import numpy
import cv2

while True:
    img = pyautogui.screenshot()  # it captures image every millisocond
    img_np = numpy.array(img)  # numpy array stores all the screenshots inside a array format
    cv2.imshow('Screen Recorderr', img_np)

    if cv2.waitKey(10) == ord('q'):
        break
