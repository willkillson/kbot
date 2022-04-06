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

vision_uni_a = Vision("./images/needle/items/unique_a.jpg")
vision_rar_e = Vision("./images/needle/items/rare_e.jpg")

loop_time = time()
while(True):    
    # get an updated image of the game
    screenshot = wincap.get_screenshot()
    
    # update our bot
    bot.updateState(screenshot)


    bot.vision_unique_a
    # pre-process the image
    processed_uni = bot.vision_unique_a.apply_hsv_filter(screenshot,bot.hsv_filter_unique)
    processed_rare = bot.vision_rare_e.apply_hsv_filter(screenshot,bot.hsv_filter_rare)


    # do object detection
    uniqueRectangles = vision_uni_a.find(processed_uni, 0.46)
    rareRectangles = vision_rar_e.find(processed_rare, 0.46)
    
    print("uniqueRectangles{}".format(uniqueRectangles))
    print("rareRectangles{}".format(rareRectangles))
    

    # sleep(5)
    # draw the detection results onto the original image
    output_image = vision_uni_a.draw_rectangles(screenshot, rareRectangles)

    # display the processed image
    cv.imshow('Processed', processed_rare)
    cv.imshow('Matches', screenshot)

    # debug the loop rate
    print('FPS {}'.format(1 / (time() - loop_time)))
    loop_time = time()

    # press 'q' with the output window focused to exit.
    # waits 1 ms every loop to process key presses
    if cv.waitKey(1) == ord('q'):
        cv.destroyAllWindows()
        break

print('Done.')