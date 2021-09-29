import pyautogui
import numpy
import cv2

while True:
    img = pyautogui.screenshot()  # it captures image every millisocond
    img_np = numpy.array(img)  # numpy array stores all the screenshots inside a array format
    img_rgb = cv2.cvtColor(img_np,cv2.COLOR_BGR2RGB)
    cv2.imshow('Screen Recorderr', img_rgb)

    if cv2.waitKey(10) == ord('q'):
        break
