import numpy as np 
from glob import glob
import matplotlib.pyplot as plt
from tqdm import tqdm
import argparse
import os

def parse_args():
    parser = argparse.ArgumentParser(description='calculate the mean value and std value for given dataset')
    parser.add_argument('--data_dir', help='the dir to images')
    parser.add_argument('--scale',type=int, choices=[1, 255],default=1,help='the scale of output value')
    parser.add_argument('--type',type=str, choices=['jpg', 'bmp','png','tif'],default='jpg',help='the type of image')
    args = parser.parse_args()
    return args


def scan_dataset(image_list):

    R_means = []
    G_means = []
    B_means = []

    R_stds = []
    G_stds = []
    B_stds = []

    for img_path in tqdm(image_list):
        image=plt.imread(img_path)
        im_R = image[:,:,0]
        im_G = image[:,:,1]
        im_B = image[:,:,2]

        im_R_mean = np.mean(im_R)
        im_G_mean = np.mean(im_G)
        im_B_mean = np.mean(im_B)

        im_R_std = np.std(im_R)
        im_G_std = np.std(im_G)
        im_B_std = np.std(im_B)

        R_means.append(im_R_mean)
        G_means.append(im_G_mean)
        B_means.append(im_B_mean)
        R_stds.append(im_R_std)
        G_stds.append(im_G_std)
        B_stds.append(im_B_std)

    mean = [R_means,G_means,B_means]
    std = [R_stds,G_stds,B_stds]


    mean[0] = np.mean(mean[0])
    mean[1] = np.mean(mean[1])
    mean[2] = np.mean(mean[2])

    std[0] = np.mean(std[0])
    std[1] = np.mean(std[1])
    std[2] = np.mean(std[2])

    return mean,std


if __name__=="__main__":
    args=parse_args()
    image_list=glob(os.path.join(args.data_dir,"*."+args.type))
    mean,std=scan_dataset(image_list)
    if args.scale==1:
        mean=[i/255.0 for i in mean]
        std=[i/255.0 for i in std]
    
    print('mean value for the dataset:\n[{},{},{}]'.format(mean[0],mean[1],mean[2]))
    print('std value for the dataset:\n[{},{},{}]'.format(std[0],std[1],std[2]))



