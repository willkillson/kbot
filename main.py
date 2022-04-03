#https://www.youtube.com/watch?v=KecMlLUuiE4

import cv2 as cv
from cv2 import threshold
import numpy as np

haystack_img = cv.imread("./images/haystack.png", cv.IMREAD_UNCHANGED)

needle_img = cv.imread("./images/needle_a5_town_stash.png", cv.IMREAD_UNCHANGED)

result = cv.matchTemplate(haystack_img,needle_img,cv.TM_CCOEFF_NORMED)

# get the best match position
min_val, max_val, min_loc, max_loc = cv.minMaxLoc(result)


print("best match top left position: %s" % str(max_loc))
print("best match confidence: %s" % str(max_val))

threshold = 0.8
if max_val >= threshold:
    print("found needle.")
    needle_img_w = needle_img.shape[1]
    needle_img_h = needle_img.shape[0]

    top_left = max_loc
    bottom_right = (top_left[0]+needle_img_w,top_left[1]+needle_img_h)
    
    cv.rectangle(haystack_img, top_left,bottom_right,color=(0,255,0),thickness=2,lineType=cv.LINE_4)
    cv.imshow("result", haystack_img)
    cv.waitKey()

else:
    print("needle not found")






