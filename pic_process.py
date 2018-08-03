import numpy as np
import cv2
import os

font= cv2.FONT_HERSHEY_SIMPLEX
data_dir = "E:\\BUAA\\dataset\\7\\height"
for fname in os.listdir(data_dir):
    fpath = os.path.join(data_dir, fname)  # path of the files
    img = cv2.imread(fpath)
    cv2.putText(img,'Unknown!',(0,130),font,1,(200,255,255),2,cv2.LINE_AA)
    path = 'E:\\BUAA\\dataset\\framez\\'
    cv2.imwrite(path + fname, img)
    print("file: " + fname + " saved")