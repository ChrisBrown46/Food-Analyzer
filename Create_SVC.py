#!/usr/bin/python

import os, os.path
import json
from sklearn import svm
import numpy as np
from sklearn.externals import joblib


# Variable must be changed to match the directory of image tags.
IMG_DIR = open('config', 'r').readlines()[3]



# Create the linear SVC
svc = svm.SVC(kernel = 'linear')


# Retrieve the training data and store it as X and Y
X = []
Y = []
for path, dir_list, file_list in os.walk(IMG_DIR + '/Image_Tags/'):
    for tag_file in file_list:
        for x in xrange(49):
            Y.append(tag_file[4:-4])
            
        lines = [json.loads(line) for line in
                 open(IMG_DIR + '/Image_Tags/' + tag_file, 'r')]
        
        for line in lines:
            X.append(line)   
X = np.array(X)


# Train the SVC
svc.fit(X, Y)


# Save the training in a pickle file
joblib.dump(svc, 'Training.pkl')

