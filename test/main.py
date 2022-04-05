import cv2 as cv
import numpy as np
import os
from time import time
from windowcapture import WindowCapture
from vision import Vision
from hsvfilter import HsvFilter

# Change the working directory to the folder this script is in.
# Doing this because I'll be putting the files from each video in their own folder on GitHub
os.chdir(os.path.dirname(os.path.abspath(__file__)))


# initialize the WindowCapture class
wincap = WindowCapture()
# initialize the Vision class
vision_uni_a = Vision('./items/unique_a.jpg')
# initialize the trackbar window
# vision_limestone.init_control_gui()

# limestone HSV filter
hsv_filter = HsvFilter(0, 180, 129, 15, 229, 243, 143, 0, 67, 0)

hsv_filter_rare = HsvFilter(26, 122, 0, 39, 170, 255, 3, 16, 0, 0)
hsv_filter_unique = HsvFilter(17, 71, 166, 27, 118, 203, 11, 24, 0, 0)


loop_time = time()
while(True):

    # get an updated image of the game
    screenshot = wincap.get_screenshot()

    # pre-process the image
    processed_image = vision_uni_a.apply_hsv_filter(screenshot,hsv_filter_unique)

    # do object detection
    rectangles = vision_uni_a.find(processed_image, 0.46)

    # draw the detection results onto the original image
    output_image = vision_uni_a.draw_rectangles(screenshot, rectangles)

    # display the processed image
    cv.imshow('Processed', processed_image)
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
