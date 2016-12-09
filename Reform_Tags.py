#!/usr/bin/python
# Requires the tags to be created through 'Food_Analyzer.py' before use.

import sys
import os
import fnmatch
import json

# Variable must be changed to match the directory of image tags.
IMG_DIR = open('config', 'r').readlines()[3]


# Reads all files from 'Image_Tags' folder then generates
# a file called 'Image_Tags.txt' which has the number of
# unique tags, and a JSON object of all the unique tags
tag_dictionary = {}
pat = r'\], \['
for path, dir_list, file_list in os.walk(IMG_DIR + '/Image_Tags/'):
    for tag_file in file_list:
        tag_file = open(IMG_DIR + '/Image_Tags/' + tag_file, 'r')
        tags_list = tag_file.read()
        tags_list = json.loads(tags_list)
        tag_file.close()

        for tags in tags_list:
            for tag in tags:
                tag_dictionary[tag] = 0

total_tags_array = [key for key in tag_dictionary]
open('Image_Tags.txt', 'w').close()
f = open('Image_Tags.txt', 'a')
f.write(json.dumps(total_tags_array))
f.close()


# Goes through all the files in 'Image_Tags' and changes
# the JSON objects so they are 1's and 0's and correspond
# to the large tag collection created prior.

for path, dir_list, file_list in os.walk(IMG_DIR + '/Image_Tags/'):
    for tag_file in file_list:
        f = open(IMG_DIR + '/Image_Tags/' + tag_file, 'r')
        tags_list = f.read()
        tags_list = json.loads(tags_list)
        f.close()
        f = open(IMG_DIR + '/Image_Tags/' + tag_file, 'w')
        
        for tags in tags_list:
            copy_array = list(total_tags_array)
            for n, i in enumerate(copy_array):
                if i in tags:
                    copy_array[n] = 1
                else:
                    copy_array[n] = 0
            f.write(json.dumps(copy_array))
            f.write('\n')
        f.close()
        
