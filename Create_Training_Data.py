#!/usr/bin/python

import sys
import os
import fnmatch
import json
from clarifai import rest
from clarifai.rest import ClarifaiApp
from Create_Tags import generate_tags_for_image


# Variable must be changed to match the directory of images being read.
# The directory should contain folders with pictures of food inside of
# each; in addition the sub-directories should be the name of the
# food the pictures are of.

IMG_DIR = open('config', 'r').readlines()[3]


# GEN_ANALYZE_ALL_IMAGES Generator that yields a food name, and the
# tags associated with it. Requires a valid IMG_DIR assigned at
# the top of the file.

def gen_analyze_all_images():
    for path, dir_list, file_list in os.walk(IMG_DIR):
        for directory in dir_list:
            for sub_path, sub_dir_list, sub_file_list in os.walk(path + '/' + directory):
                for image in sub_file_list:
                    food_group = directory
                    image_path = sub_path + '/' + image
                    yield (food_group, generate_tags_for_image(image_path, 'file'))


# CREATE_TRAINING_DATA Creates a set of training data that is stored
# in 'Tag_(food_item).txt'. No arguments are needed, and there are no returns.
# The only requirement is that there is a valid IMG_DIR.

def create_training_data():
    # Create a list of tags for a food and store it in Image_Tags/Tag_Food
    previous_food = ''
    text_file = 0
    
    # Loop through each picture and take what food it is,
    # and what tags it receives
    for food_group, tags in gen_analyze_all_images():
        # When a food group finishes, write it to a file
        # then start the next food group.
        if food_group != previous_food:
            if text_file:
                text_file.write(json.dumps(food_list))
                text_file.close()
            food_list = []
            text_file = open('Image_Tags/Tag_' + food_group + '.txt', 'a')
        
        food_list.append(tags)
        previous_food = food_group
    text_file.write(json.dumps(food_list))
    text_file.close()
