import os
import re
import random
import matplotlib.pyplot as plt
import cv2
import numpy as np
import urllib.request
from urllib.parse import quote
import httplib2
import pynder
from keras import optimizers
from keras.applications.vgg16 import VGG16
from keras.layers import Dense, Dropout, Flatten, Input
from keras.models import Model, Sequential, load_model
from keras.utils.np_utils import to_categorial

def get_image(img_url):
    opener = urllib.request.build_opener()
    http = httplib2.Http(".cache")
    response, content = http.request(img_url)
    return content

def aidemy_imshow(name, img):
    b,g,r = cv2.split(img)
    img = cv2.merge([b,g,r])
    plt.imshow(img)
    plt.show()
cv2.imshow = aidemy_imshow

def jpg_count(folder_name):
    files = os.listdir("./"+folder_name)
    jpgcount = 0
    for file in files:
        index = re.search(".jpg", file)
        if index:
            jpgcount += 1
    return jpgcount

def image_save(img, folder_name):
    if not os.path.exists(folder_name):
        os.mkdir(folder_name)
    jpgcount = jpg_count(folder_name)
    w_pass = "./{}/{}.jpg".format(folder_name, jpgcount)
    cv2.imshow(w_pass, img)

