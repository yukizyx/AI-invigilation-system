import cv2
from PIL import Image
from dlib import rectangle
import numpy as np

def cv2_2_pil(img):
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img = Image.fromarray(img)
    return img

def pil_2_cv2(img):
    img = cv2.cvtColor(np.asarray(img), cv2.COLOR_RGB2BGR)
    return img

def bb_2_rect(bb):
    bb = [int(i) for i in bb]
    return rectangle(bb[0], bb[1], bb[2], bb[3])

def dist_2d(p1, p2):
    return np.sqrt((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)

def mid_point_2d(p1, p2, to_int = False):
    pt = ((p1[0]+p2[0])/2, (p1[1]+p2[1])/2)
    if to_int == True:
        pt = (int(pt[0]), int(pt[1]))
        return pt
    return pt

def sigmoid(z):
    return 1/(1 + np.exp(-z))