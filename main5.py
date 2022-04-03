from tkinter import Image
import cv2 as cv
import numpy as np
from time import time
from WindowCapture import WindowCapture

wincap = WindowCapture("Diablo II: Resurrected")

loop_time = time()
while(True):
   

    screenshot = wincap.get_screenshot()

    cv.imshow("Computer Vision", screenshot)

    print("FPS {}".format(1/(time()-loop_time)))
    loop_time = time()


    # press q with output window focused to exit
    # waits 1 ms every loop to process key presses
    if cv.waitKey(1) == ord("q"):
        cv.destroyAllWindows()
        break
