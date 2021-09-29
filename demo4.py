import pyautogui
import numpy
import cv2
from win32api import GetSystemMetrics

screen_width = GetSystemMetrics(0)
screen_height= GetSystemMetrics(1)

fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')
video = cv2.VideoWriter('videoo.mp4', fourcc, 10.0, (1920, 1080))

while True:
    img = pyautogui.screenshot()  # it captures image every millisocond
    img_np = numpy.array(img)  # numpy array stores all the screenshots inside a array format
    img_rgb = cv2.cvtColor(img_np,cv2.COLOR_BGR2RGB)
    cv2.imshow('Screen Recorderr', img_rgb)
    video.write(img_rgb)

    if cv2.waitKey(10) == ord('q'):
        break
