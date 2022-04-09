#https://www.youtube.com/watch?v=m1pbF9BW8tA

import cv2 as cv
from cv2 import threshold
from cv2 import MARKER_CROSS
import numpy as np

def findClickPositions(haystack_img_path,needle_img_path, threshold = 0.5, debug_mode=None):
    haystack_img = cv.imread(haystack_img_path, cv.IMREAD_UNCHANGED)
    needle_img = cv.imread(needle_img_path, cv.IMREAD_UNCHANGED)
    needle_img_w = needle_img.shape[1]
    needle_img_h = needle_img.shape[0]
    
    result = cv.matchTemplate(haystack_img,needle_img,cv.TM_CCOEFF_NORMED)
    locations = np.where(result >= threshold)
    locations = list(zip(*locations[::-1]))

    #first we need to create the list of  [x,y,w,h] rectangles
    rectangles = []
    for loc in locations:
        rect = [int(loc[0]), int(loc[1]), needle_img_w, needle_img_h]
        rectangles.append(rect)

    #group the rectangles to reduce the duplicates
    rectangles, weights = cv.groupRectangles(rectangles,1,0.5)    

    if len(rectangles):
        line_color = (0,255,0)
        line_type = cv.LINE_4
        marker_color = (255,0,255)
        marker_type = cv.MARKER_CROSS

        clickPoints = []
        for(x,y,w,h) in rectangles:
            top_left = (x,y)
            bottom_right = (x+w, y+h)
            cv.rectangle(
                haystack_img,
                top_left,
                bottom_right,line_color,line_type)
            center_x = x + int(w/2)
            center_y = y + int(h/2)
            clickPoints.append((center_x,center_y))
            cv.drawMarker(haystack_img,(center_x,center_y), marker_color,marker_type)
    return clickPoints