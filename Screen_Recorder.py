import pyautogui
import numpy
import cv2
from win32api import GetSystemMetrics
import datetime as dt

screen_width = GetSystemMetrics(0)
screen_height= GetSystemMetrics(1)

current_dt = dt.datetime.now().strftime('%d-%m-%Y %I-%M-%S')
file_name = current_dt + '.mp4'

# we need infinite loop to run any software we can manually create it by while loop

fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')
video = cv2.VideoWriter(file_name, fourcc, 10.0, (1920, 1080))
#                       filename  videoformat  speedofVideoRecord  sizeofScreen

while True:
    img = pyautogui.screenshot()  # it captures image every millisocond
    img_np = numpy.array(img)  # numpy array stores all the screenshots inside a array format
    img_rgb = cv2.cvtColor(img_np, cv2.COLOR_BGR2RGB)
    cv2.imshow('Screen Recorder', img_rgb)
    video.write(img_rgb)

    if cv2.waitKey(10) == ord('q'):
        break
