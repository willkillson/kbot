import cv2 as cv
import numpy as np
import os
from time import time
from windowcapture import WindowCapture
from vision import Vision
import pyautogui
from time import sleep, time

# Change the working directory to the folder this script is in.
# Doing this because I'll be putting the files from each video in their own folder on GitHub
os.chdir(os.path.dirname(os.path.abspath(__file__)))


# initialize the WindowCapture class
wincap = WindowCapture()
# initialize the Vision class
vision_stash = Vision('./images/needle/stash_a5.jpg')
vision_stairs1 = Vision('./images/needle/a5_stairs1.jpg')
vision_stairs2 = Vision('./images/needle/a5_stairs2.jpg')

'''
# https://www.crazygames.com/game/guns-and-bottle
wincap = WindowCapture()
vision_gunsnbottle = Vision('gunsnbottle.jpg')
'''

loop_time = time()
while(True):

    # get an updated image of the game
    screenshot = wincap.get_screenshot()

    # display the processed image
    points = vision_stash.find(screenshot, 0.5, 'rectangles')
    # points = vision_stairs1.find(screenshot, 0.5, 'rectangles')
    # points = vision_stairs2.find(screenshot, 0.5, 'rectangles')

    #points = vision_gunsnbottle.find(screenshot, 0.7, 'points')

    pyautogui.moveTo(wincap.w/2,wincap.h/2);
    pyautogui.click();
    sleep(5)




    # debug the loop rate
    print('FPS {}'.format(1 / (time() - loop_time)))
    loop_time = time()

    # press 'q' with the output window focused to exit.
    # waits 1 ms every loop to process key presses
    if cv.waitKey(1) == ord('q'):
        cv.destroyAllWindows()
        break

print('Done.')