#!/usr/bin/python

import os, os.path
import json
import sys
import numpy as np
from sklearn import svm
from sklearn.externals import joblib
from Create_Tags import generate_tags_for_image

# Not ideal, but warnings are not relevant at the time.
# Remove to see warnings and fix if issues occur
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)


def classify_file(filepath, method):
    
    # First generate tags for the image, then open our SVC
    # and super tag list
    output = generate_tags_for_image(filepath, method)
    output = output[5:]
    svc = joblib.load('Training.pkl')
    tags = json.loads(open('Image_Tags.txt', 'r').read())

    # Turn our recieved tags into a sparse array that is
    # based off of our super tag list
    sparse_array = []
    for tag in tags:
        if tag in output:
            sparse_array.append(1)
        else:
            sparse_array.append(0)
    sparse_array = np.array(sparse_array)

    return svc.predict(sparse_array)[0]


IMG_DIR = open('config', 'r').readlines()[3]
def gen_analyze_all_images():
    for path, dir_list, file_list in os.walk(IMG_DIR + '/Images/'):
        for directory in dir_list:
            for sub_path, sub_dir_list, sub_file_list in os.walk(path + '/' + directory):
                for image in sub_file_list:
                    food_group = directory
                    image_path = 'Images/' + food_group + '/' + image
                    yield (food_group, classify_file(image_path, 'file'))

                    
def create_side_list():
    side_list = {}

    for food_group, side in gen_analyze_all_images():
        if side == food_group:
            print '.'
            continue
        
        if food_group in side_list:
            side_list[food_group].append(side)
        else:
            side_list[food_group] = [side]
        
        f = open('Sides.txt', 'w')
        f.write(json.dumps(side_list))
        f.close()

    condense_side_list()


import operator
def condense_side_list():
    side_list = json.loads(open('Sides.txt', 'r').read())
    for food in side_list:
        temp_dict = {}
        for side in side_list[food]:
            if side in temp_dict:
                temp_dict[side] += 1
            else:
                temp_dict[side] = 1
                
        sorted_list = sorted(temp_dict.items(), key=operator.itemgetter(1), reverse=True)
        sorted_list = sorted_list[:3]

        side_list[food] = [sorted_list[0][0], sorted_list[1][0], sorted_list[2][0]]

    f = open('Sides.txt', 'w')
    f.write(json.dumps(side_list))
    f.close()
    
def get_sides(food):
    side_list = json.loads(open('Sides.txt', 'r').read())
    for food in side_list[food]:
        print food
    return side_list[food]

