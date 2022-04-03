from tkinter import Image
import cv2 as cv
import numpy as np
import pyautogui

from time import time
from PIL import ImageGrab

import win32gui
import win32ui
import win32con

def window_capture():

    w = 1920
    h = 1080

    hwnd = win32gui.FindWindow(None, "Diablo II: Resurrected")
    # hwnd = None
    
    wDC = win32gui.GetWindowDC(hwnd)
    dcObj = win32ui.CreateDCFromHandle(wDC)
    cDC = dcObj.CreateCompatibleDC()
    dataBitMap = win32ui.CreateBitmap()
    dataBitMap.CreateCompatibleBitmap(dcObj,w,h)
    cDC.SelectObject(dataBitMap)
    cDC.BitBlt((0,0),(w,h),dcObj,(0,0),win32con.SRCCOPY)

    #save the screen shot
    dataBitMap.SaveBitmapFile(cDC,"debug.bmp")

    signedIntsArray = dataBitMap.GetBitmapBits(True)
    img = np.fromstring(signedIntsArray,dtype='uint8')
    img.shape = (h,w,4)

    #free resources
    dcObj.DeleteDC()
    cDC.DeleteDC()
    win32gui.ReleaseDC(hwnd,wDC)
    win32gui.DeleteObject(dataBitMap.GetHandle())

    #drop alpha channel
    img = img[...,:3]

    #because of an error
    img = np.ascontiguousarray(img)

    return img

loop_time = time()
while(True):
   
    # #convert screenshot
    # screenshot = ImageGrab.grab()
    # # screenshot = pyautogui.screenshot()
    # screenshot = np.array(screenshot)
    # # screenshot = screenshot[:,:,::-1].copy()
    # screenshot = cv.cvtColor(screenshot,cv.COLOR_RGB2BGR)
    
    screenshot = window_capture()

    cv.imshow("Computer Vision", screenshot)

    print("FPS {}".format(1/(time()-loop_time)))
    loop_time = time()


    # press q with output window focused to exit
    # waits 1 ms every loop to process key presses
    if cv.waitKey(1) == ord("q"):
        cv.destroyAllWindows()
        break
