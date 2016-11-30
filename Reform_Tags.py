#!/usr/bin/python
# Requires the tags to be created through 'Food_Analyzer.py' before use.

import sys
import os
import fnmatch
import json

# Variable must be changed to match the directory of images being read.
# The directory should contain folders with pictures of food inside of
# each; in addition the sub-directories should be the name of the
# food the pictures are of.

IMG_DIR = 'D:/Personal/School/Third Year/CS 5600/Food Analyzer'


# Reads all files from 'Image_Tags' folder then generates
# a file called 'Image_Tags.txt' which has the number of
# unique tags, and a JSON object of all the unique tags
tag_dictionary = {}
pat = r'\], \['
for path, dir_list, file_list in os.walk(IMG_DIR + '/Image_Tags/'):
    for tag_file in file_list:
        tag_file = open(IMG_DIR + '/Image_Tags/' + tag_file)
        tags = tag_file.read()
        tags = json.loads(tags)
        tag_file.close()

        for tag in tags:
            for item in tag:
                tag_dictionary[item] = 0

open('Image_Tags.txt', 'w').close()
f = open('Image_Tags.txt', 'a')
f.write(str(len(tag_dictionary)))
f.write('\n')
f.write(json.dumps(tag_dictionary))
f.close()


# Goes through all the files in 'Image_Tags' and changes
# the JSON objects so they are 1's and 0's and correspond
# to the large tag collection created prior.
