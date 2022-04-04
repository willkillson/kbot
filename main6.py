import cv2 as cv
import sys
from time import time
from windowcapture import WindowCapture
from vision import Vision
from time import sleep, time
from bot import kbot

# initialize the WindowCapture class
wincap = WindowCapture()
bot = kbot()

loop_time = time()
while(True):
    # get an updated image of the game
    screenshot = wincap.get_screenshot()
    bot.updateState(screenshot)
    
    
       

    # display the processed image
    # points = vision_login_a1.find(screenshot, 0.5, 'rectangles')
    # points = vision_stairs1.find(screenshot, 0.5, 'rectangles')
    # points = vision_stairs2.find(screenshot, 0.5, 'rectangles')

    #points = vision_gunsnbottle.find(screenshot, 0.7, 'points')
    # print(len(points))

    # pyautogui.moveTo(wincap.w/2,wincap.h/2);
    # pyautogui.click();
    # sleep(5)
    

    # debug the loop rate
    print('FPS {}'.format(1 / (time() - loop_time)))
    loop_time = time()
    

    # press 'q' with the output window focused to exit.
    # waits 1 ms every loop to process key presses
    if cv.waitKey(1) == ord('q'):
        cv.destroyAllWindows()
        break

print('Done.')