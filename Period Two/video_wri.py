import cv2
import os

path = "analysisvideo.avi"
fps = 16   #视频帧率
fourcc = cv2.VideoWriter_fourcc(*'IYUV')
videoWriter = cv2.VideoWriter(path, -1, fps, (480, 800))

#(1360,480)为视频大小
data_dir = "E:\\BUAA\\dataset\\framez"
fname = "height_pic"
form = ".jpg"
for i in range(1, 1893):
    name = fname + str(i) + form
    fpath = os.path.join(data_dir, name)  # path of the files
    print("process frame " + name)
    img = cv2.imread(fpath)
    #print(img.shape)
    #cv2.imshow('img', img)
    #cv2.waitKey(int(1000/fps))
    videoWriter.write(img)

videoWriter.release()
