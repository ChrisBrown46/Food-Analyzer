import sys
import json
from clarifai import rest
from clarifai.rest import ClarifaiApp
import os, os.path
import numpy as np
from sklearn import svm
from collections import defaultdict
from sklearn.externals import joblib
from sklearn import preprocessing
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
import ast

with open('config') as f:
    credentials = f.read().splitlines()

# Create a food model for Clarifai
app = ClarifaiApp(credentials[0], credentials[1])
model = app.models.get("food-items-v1.0")

clf = svm.SVC(kernel='linear')

def train():


    # reading in the images for training
    Path = "Image_Tags/Tag_apple_pie.txt"
    Path2 = "Image_Tags/Tag_baby_back_ribs.txt"
    labelPath = "images2"

    testTarget = []
    foodList = []


    labelNum = 1

    for item in os.listdir(labelPath):
        for image in os.listdir(labelPath + "/" + item):

            output = model.predict_by_filename(filename=labelPath + "/" + item + "/" + image)
            output = output[u'outputs'][0][u'data'][u'concepts']

            for food in output:
                foodList.append(food[u'name'])

            count_vect = CountVectorizer()
            training = count_vect.fit_transform(foodList)

            print training.shape
            for count in xrange(training.shape[0]):
                testTarget.append(count)

            clf.fit(training, testTarget)
            joblib.dump(clf, 'test.pkl')

            del foodList[:]
            del testTarget[:]


def test():
    clf2 = joblib.load('test.pkl')

    testList = []
    testOutput = model.predict_by_filename('applePieTest.jpg')
    testOutput = testOutput[u'outputs'][0][u'data'][u'concepts']
    for testFood in testOutput:
        testList.append(testFood['name'])

    testVector = CountVectorizer()
    test1 = testVector.fit_transform(testList)

    print test1.shape
    prediction = clf2.predict(test1)

    print prediction




test()