#https://www.youtube.com/watch?v=ffRYijPR8pk

import cv2 as cv
from cv2 import threshold
import numpy as np

haystack_img = cv.imread("./images/haystack/haystack_a5_frigid_eldritch.png", cv.IMREAD_UNCHANGED)

needle_img = cv.imread("./images/needle/login/login_a1.jpg", cv.IMREAD_UNCHANGED)
needle_img_w = needle_img.shape[1]
needle_img_h = needle_img.shape[0]

result = cv.matchTemplate(haystack_img,needle_img,cv.TM_CCOEFF_NORMED)



threshold = 0.25
locations = np.where(result >= threshold)



# we can zip those up into position tuples
locations = list(zip(*locations[::-1]))

print(locations)
for loc in locations:
    #determine box pos
    top_left = loc
    bottom_right = (top_left[0]+needle_img_w, top_left[1]+needle_img_h)
    #draw box
    cv.rectangle(haystack_img,top_left,bottom_right,color=(0,255,0),lineType=cv.LINE_4)

cv.imshow("result", haystack_img)
cv.waitKey()
