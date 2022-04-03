#https://www.youtube.com/watch?v=m1pbF9BW8tA

import cv2 as cv
from cv2 import threshold
from cv2 import MARKER_CROSS
import numpy as np

# Custom function
from findClickPositions import findClickPositions

clickPositions = findClickPositions(
    "./images/haystack/haystack_a5_frigid_eldritch.png",
    "./images/needle/needle_a5_frigid_eldritch_minnion.png",
    0.25,
    None)

print(clickPositions)
