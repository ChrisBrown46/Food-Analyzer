#!/usr/bin/python

import os, os.path
import json
import sys
import numpy as np
from sklearn import svm
from sklearn.externals import joblib
from Create_Training_Data import generate_tags_for_image


def classify_file(filepath):
    # First generate tags for the image, then open our SVC
    # and super tag list
    output = generate_tags_for_image(filepath)
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
print classify_file(sys.argv[1])
