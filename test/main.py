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
vision_rar_e = Vision('./items/rare_e.jpg')

vision_malah = Vision('./malah/malah_filtered.jpg')
vision_malah2 = Vision('./malah/malah_filtered_2.jpg')
vision_malah3 = Vision('./malah/malah_filtered_3.jpg')
vision_malah4 = Vision('./malah/malah_filtered_4.jpg')
# initialize the trackbar window
# vision_limestone.init_control_gui()

# limestone HSV filter
hsv_filter = HsvFilter(0, 180, 129, 15, 229, 243, 143, 0, 67, 0)

# malah_filter
malah_filter = HsvFilter(0, 0, 82, 179, 86, 255, 48, 0, 100, 119)
vision_malah.init_control_gui();

# hsv_filter_rare = HsvFilter(26, 122, 0, 39, 170, 255, 3, 16, 0, 0)
# hsv_filter_unique = HsvFilter(17, 71, 166, 27, 118, 203, 11, 24, 0, 0)


loop_time = time()
while(True):

    # get an updated image of the game
    screenshot = wincap.get_screenshot()
    
    # processed_image = vision_malah.apply_hsv_filter(screenshot)

    processed_image = vision_malah.apply_hsv_filter(screenshot,malah_filter)

    # do object detection
    malahRect1 = vision_malah.find(processed_image, 0.45)
    malahRect2 = vision_malah2.find(processed_image,0.45)
    malahRect3 = vision_malah3.find(processed_image,0.45)
    malahRect4 = vision_malah4.find(processed_image,0.45)
    allRectangles =  [*malahRect1, *malahRect2, * malahRect3, *malahRect4]
    
    print(allRectangles)
    
    # draw the detection results onto the original image
    output_image = vision_malah.draw_rectangles(screenshot, allRectangles)

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
