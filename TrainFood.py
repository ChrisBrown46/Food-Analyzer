import sys
import json
from clarifai import rest
from clarifai.rest import ClarifaiApp
import os, os.path
import numpy as np
import scipy
from sklearn import svm
from collections import defaultdict
from sklearn.externals import joblib
from PIL import Image
from sklearn.feature_extraction.text import CountVectorizer
import scipy

classification = svm.SVC()


def train():
    with open('config') as f:
        credentials = f.read().splitlines()

    # Create a food model for Clarifai
    app = ClarifaiApp(credentials[0], credentials[1])
    model = app.models.get("food-items-v1.0")

    foodList = []
    foodLabel = []
    folders = []

    # reading in the images for training
    foodPath = "images"

    for item in os.listdir(foodPath):

        for image in os.listdir(foodPath + "/" + item):

            output = model.predict_by_filename(filename=foodPath + "/" + item + "/" + image)
            output = output[u'outputs'][0][u'data'][u'concepts']
            for food in output:
                foodList.append(food['name'])

            for x in xrange(len(foodList)):
                foodLabel.append(x+1)

            vectorizer = CountVectorizer(min_df=1)

            X = vectorizer.fit_transform(foodList)
            print len(X.toarray())

            classification.fit(np.array(foodLabel).reshape(len(foodLabel), 1), X)
            print "done"
            del foodList[:]
            del foodLabel[:]
            del X

        #joblib.dump(classification, 'training.pkl')
        joblib.dump(classification, str(item) + '.pkl')
        print "done"

def test():
    with open('config') as f:
        credentials = f.read().splitlines()

    # Create a food model for Clarifai
    app = ClarifaiApp(credentials[0], credentials[1])
    model = app.models.get("food-items-v1.0")
    testFood = []
    classification = joblib.load('training.pkl')

    output = model.predict_by_filename(filename='applePieTest.jpg')
    output = output[u'outputs'][0][u'data'][u'concepts']

    for food in output:
        testFood.append((food['name']))

    vectorizer = CountVectorizer(min_df=1)

    X = vectorizer.fit_transform(testFood)
    label = classification.predict(X)
    print label

train()