# step1: turn jpg to numpy array
# step2: turn numpy array to tensor and proprocess the data
# step3: turn the tensors to the numpy array to the csv files
import os
import numpy as np
import tensorflow as tf
import random
import shutil


def data2csv(data_dir, label_name):
    """
    convert the image to the numpy csv files
    :param data_dir: the working directory  C:\\dd\\dd
    :param label_name: the labels of images  'label_height/reflection'
    :return: 0
    """
    number = 0
    for fname in os.listdir(data_dir):
        number += 1
        '''
        if number <= 720:
            print("process file: " + str(number))
            continue
        '''
        fileName = label_name + str(number)
        print("process file: " + fileName)
        fpath = os.path.join(data_dir, fname) # path of the files

        with tf.gfile.FastGFile(fpath, 'rb') as f:
            image_data = f.read()
        with tf.Session() as sess:
            image_data = tf.image.decode_jpeg(image_data)
            image = sess.run(image_data)

        #image = Image.open(fpath) # load the image
        #data = np.array(image)
        print(image.shape)
        # convert numpy array to tensor
        #ten_data = tf.convert_to_tensor(data)
        # preprocess the image
        ten_data = tf.image.resize_image_with_crop_or_pad(image, 480, 480)
        ten_data = tf.image.resize_images(ten_data, [28, 28], method=0)
        # convert the tensor to the numpy data type
        sess = tf.Session()
        with sess.as_default():
            data = ten_data.eval()
        sess.close()
        # write into the csv files, the first parameter is the directory

        np.savetxt(fileName+'.csv', data, fmt='%d', delimiter=",")
        # load the file：
        # the label can be got by the name of the file
    return 0

def create_random(total):
    iterate = round(total * 0.2)
    start = 1
    stop = total
    random_list = []
    for i in range(iterate):
        random_list.append(random.randint(start, stop))
    return random_list

def split_dataset(src_dir, des_dir, random_list):
    number = 0
    for fname in os.listdir(src_dir):
        fpath = os.path.join(src_dir, fname)  # path of the files
        number += 1
        print("process #:" + str(number))
        if number in random_list:
            shutil.move(fpath, des_dir)
        else:
            pass
    return 0

def load_data(data_dir):
    """
    load the training data for training
    :param data_dir: the directory of the csv files
    :return: (training data and training labels array)
    """
    train_data = []
    train_labels = []
    number = 0
    for fname in os.listdir(data_dir):
        number += 1
        #print("process file: " + fname)
        fpath = os.path.join(data_dir, fname) # path of the files
        data = np.loadtxt(open(fpath, "rb"), delimiter=",")  # python array data structure
        train_data.append(data)
        label = int(fname[0])
        train_labels.append(label)
    train_data = np.array(train_data).reshape((number, 28, 28, 1))
    train_labels = np.array(train_labels).reshape((number, 1))
    return (train_data, train_labels)

if __name__ == "__main__":
    #data2csv("E:\\BUAA\\实验室\\阶段2：\\数据集\\右侧90°丁字路_6\\高度", "6_height")
    #random_list = create_random(65)
    #split_dataset("E:\\BUAA\\实验室\\阶段2：\\class_2\\height", \
    #             "E:\\BUAA\\实验室\\阶段2：\\class_2\\height_test", random_list)
    (data, label) = load_data("E:\\BUAA\\实验室\\阶段2：\\class_2\\height")
    print(data.shape, label.shape)

