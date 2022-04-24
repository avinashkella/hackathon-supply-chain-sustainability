import numpy as np
import cv2
from matplotlib import pyplot as plt



def depthMap(imgL, imgR):

    stereo = cv2.createStereoBM(numDisparities=16, blockSize=15)
    disparity = stereo.compute(imgL,imgR)
    
    return disparity