from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import os
import sys
import shutil
import logging
import argparse


import cv2
import numpy as np 

# Using torch
import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.nn.utils.weight_norm as weightNorm
import torch.optim as optim
from torch.autograd import Variable
from torch.utils.tensorboard import SummaryWriter
import torchvision

# Using tensorflow
import tensorflow as tf
from tensorflow.keras.layers import Dense, Flatten, Conv2D
from tensorflow.keras import Model

# An efficient dataflow loading for training and testing
import tensorpack.dataflow as df
import tqdm

#
# Global configuration
#
BATCH = 32
EPOCH = 500
SHAPE = 256
NF = 64

#
# Create the data flow using tensorpack dataflow (independent from tf and pytorch)
#
# TODO

#
# Create the model
#
# TODO

#
# Perform sample
#
# TODO

#
# Main
#
if __name__ == '__main__':
    #
    parser = argparse.ArgumentParser()
    parser.add_argument('--data', help='the image directory')
    parser.add_argument('--load', help='load model')
    parser.add_argument('--gpu', help='comma separated list of GPU(s) to use.')
    parser.add_argument('--sample', action='store_true', help='run inference')
    args = parser.parse_args()
    
    # Choose the GPU
    if args.gpu:
        os.environ['CUDA_VISIBLE_DEVICES'] = args.gpu
        
    if args.sample:
        # TODO: Run the inference
        pass
    else
        #
        # Train from scratch or load the pretrained network
        #
        # TODO: Load the pretrained model
        if args.load:
            pass
            
        # Initialize the program
        writer = SummaryWriter()
        use_cuda = torch.cuda.is_available()
        step = 0